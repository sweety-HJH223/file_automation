# file_automation

A Python automation script that organizes files from a source folder into appropriate destination folders such as Music, Images, Videos, and Documents.  
Designed to work in **batch mode** (not real-time) for automation tasks.

## 🚀 Features

- Automatically organizes files from a source folder  
- Categorizes files by type:
  - Audio / Music
  - Images
  - Videos
  - Documents
- Handles **duplicate filenames** safely by renaming them
- Generates a **CSV log** (`file_log.csv`) with:
  - File name
  - Source path
  - Destination path
  - Timestamp

## 📁 Supported File Types

| Category   | Extensions |
|-----------|------------|
| Audio / SFX | `.mp3`, `.wav`, `.aac`, `.m4a` |
| Images    | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Videos    | `.mp4`, `.avi`, `.mkv` |
| Documents | `.pdf`, `.docx`, `.txt`, `.pptx` |


##  How It Works

1. The script scans the source folder (`Downloads`)
2. Detects file type based on extension and size
3. Moves files to predefined destination folders
4. Renames files if a duplicate name exists
5. Logs every move into `file_log.csv`

This is a **one-time batch script**, not a real-time.

## How to Run

1. Make sure Python 3 is installed  
2. Update folder paths in the script if needed  
3. Run the script:

```bash
python file_organizer.py
Files will be organized automatically
