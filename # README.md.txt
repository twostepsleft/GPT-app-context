# README.md

## Folder Structure and File Content Extractor

This script is designed to provide developers with a quick way to extract the folder structure and content of specific files from a provided directory. The output is beneficial for applications, like GPT-4, that may require an understanding of the project structure and specific file contents for contextual processing.

### How it works:

1. **Folder Traversal**: The script begins by traversing through every folder and file in the given directory.
2. **File Content Extraction**: For each file found, its content is extracted up to a default limit of 1 MB. However, you can adjust this limit inside the script if needed.
3. **Exclusion Filters**: Users can specify which file types or specific files to ignore during the extraction process.
4. **Output**: The resulting folder structure and file content are saved into a `current_scripts.txt` file in the provided directory.

### Getting Started:

#### Prerequisites:
Ensure you have Python installed on your machine.

#### Running the Script:

1. Navigate to the directory containing the script.
2. Run the script using the following command:
    ```
    python [script_name].py
    ```

3. You'll be prompted to input the directory path that you want to extract the folder structure and content from.
4. The script will display the unique file types it finds in the directory. 
5. You'll then be asked which file types or names to ignore. Input them separated by commas. (e.g., `.pyc,.txt`)
6. Once done, the script will generate the `current_scripts.txt` file in the provided directory. This file will contain the directory structure and content of files.

### Customizing the Script:

1. **Adjusting the Maximum File Size for Content Read**: The default limit for reading a file's content is set at 1 MB. If you want to adjust this limit, search for the `max_file_size` variable inside the script and modify its value.

2. **Handling Unreadable Files**: The script handles files that can't be read due to encoding issues or permission restrictions. If such a file is encountered, the output will indicate this with a note (`[binary or unreadable content]`).

### Feedback and Contributions:

We welcome feedback, bug reports, and pull requests! 

Feel free to open an issue on this GitHub repository if you encounter problems or have suggestions.

### License:

This script is open source and available under the MIT License.

---

Happy coding!