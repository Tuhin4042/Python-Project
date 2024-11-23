# File Organizer by Type

A Python script that organizes files in a specified directory into subfolders based on their file types. This tool helps you keep your directories clean and well-organized.

---

## Features
- Automatically categorizes files based on their extensions.
- Creates folders dynamically based on file types (e.g., Images, Documents, PDFs).
- Handles common file types like `.jpg`, `.png`, `.pdf`, `.docx`, and more.
- Ensures existing folders are reused if already present.
- Easy to use: just provide the directory path as input.

---

## Supported File Types and Folders
The script organizes files into the following predefined folders:
| File Type Extensions | Folder Name         |
|-----------------------|---------------------|
| `.jpg`, `.png`, `.jpeg` | Images             |
| `.doc`, `.docx`        | Documents          |
| `.pdf`                | PDFs               |
| `.ppt`, `.pptx`       | Presentations      |
| `.txt`                | TextFiles          |
| `.ipynb`              | Python Folder      |

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `os`: For directory and file operations.
  - `shutil`: For moving files.

---

## Setup and Usage
1. Clone this repository or download the script file.
2. Ensure Python is installed on your system.
3. Open a terminal or command prompt.
4. Navigate to the script directory.
5. Run the script using:
   ```bash
   python organize_files.py

