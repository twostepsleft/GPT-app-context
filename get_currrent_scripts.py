# Required modules for the script.
import os
from pathlib import Path
from collections import defaultdict

# This function returns the hierarchical structure and content of files in the given directory.
def gather_file_structure_and_content(startpath: Path, ignored_files_and_types: list):
    # Lists to store the file structure and contents.
    file_structure = []
    file_contents = []
    
    # Define the maximum file size for which content will be read, in bytes.
    # Default is 1 MB (1,048,576 bytes). You can adjust this for different limits.
    max_file_size = 1_048_576

    # Iterate over the directory structure starting from the given path.
    for root, _, files in os.walk(startpath):
        root_path = Path(root)
        relative_path = root_path.relative_to(startpath)
        
        # Calculate the depth (level) in the directory structure.
        level = len(relative_path.parts)
        
        # Append the directory name to the file structure.
        file_structure.append('{}{}/\n'.format(' ' * 4 * level, relative_path.name))

        for file in files:
            file_path = root_path / file

            # Ignore files from reading if they're in the ignored list or their type is in the ignored list.
            if file not in ignored_files_and_types and file_path.suffix not in ignored_files_and_types:
                file_structure.append('{}|-- {}\n'.format(' ' * 4 * (level + 1), file))
                
                try:
                    # Only read the content of the file if its size is below the set maximum.
                    if file_path.stat().st_size <= max_file_size:
                        with file_path.open('r') as f:
                            content = f.read()
                        file_contents.append(f'{file}:\t{content}\n\n\n')
                    else:
                        # Indicate if the file content is too large to display.
                        file_contents.append(f'{file}:\t[content too large to display]\n\n\n')
                
                # Handle exceptions for unreadable files.
                except (UnicodeDecodeError, PermissionError):
                    file_contents.append(f'{file}:\t[binary or unreadable content]\n\n\n')

    return ''.join(file_structure), ''.join(file_contents)

# This function returns a set of unique file types/extensions present in the given directory.
def get_unique_file_types(startpath: Path):
    file_types = set()

    for _, _, files in os.walk(startpath):
        for file in files:
            file_path = Path(file)
            file_types.add(file_path.suffix)

    return file_types

def main():
    # Get directory input from the user.
    folder_location = input('Please input a folder location: ')
    folder_location = Path(folder_location)

    # Check if the provided location is a valid directory.
    if not folder_location.is_dir():
        print('Invalid folder location')
        return

    # Fetch the list of unique file types in the directory.
    unique_file_types = get_unique_file_types(folder_location)
    print("Found the following file types:", ', '.join(unique_file_types))
    
    # Get user input on which file names and/or extensions to ignore.
    ignored_input = input("Please specify which file types (including the '.' e.g. .pyc,.txt) to ignore, separated by commas: ")
    ignored_files_and_types = [item.strip() for item in ignored_input.split(",")]

    # Define the location for the output txt file and create it if doesn't exist.
    txt_file_location = folder_location / 'current_scripts.txt'
    txt_file_location.touch(exist_ok=True)

    # Get the file structure and contents.
    file_structure, all_files_content = gather_file_structure_and_content(folder_location, ignored_files_and_types)

    # Write the file structure and contents to the output txt file.
    with txt_file_location.open('w') as txt_file:
        txt_file.write(file_structure)
        txt_file.write(all_files_content)

# Start the script if it's run as the main program.
if __name__ == "__main__":
    main()
