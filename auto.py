import os
import shutil
import time
import csv

source_dir = r"C:\Users\sweet\Downloads"
dest_dirs = {
    "audio": r"C:\Users\sweet\Music",
    "music": r"C:\Users\sweet\Music",
    "images": r"C:\Users\sweet\Captures",
    "videos": r"C:\Users\sweet\Videos",
    "documents": r"C:\Users\sweet\Documents"
}

print("Batch File Organizer Started!")
print(f"Source folder: {source_dir}")
print("Destination folders:", dest_dirs)

log_file = os.path.join(dest_dirs["documents"], "file_log.csv")

#making the missing folders
for folder in dest_dirs.values():
    os.makedirs(folder, exist_ok=True)

#unique filename
def make_unique(path):
    if not os.path.exists(path):
        return path
    base, ext = os.path.splitext(path)
    counter = 1
    new_path = f"{base}({counter}){ext}"
    while os.path.exists(new_path):
        counter += 1
        new_path = f"{base}({counter}){ext}"
    return new_path


#moving files and logging
def move_files(entry, dest_key):
    dest_path = os.path.join(dest_dirs[dest_key], entry.name)
    unique_dest = make_unique(dest_path)
    shutil.move(entry.path, unique_dest)
    print(f" Moved {entry.name} → {dest_key} folder")

    # Logging
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([entry.name, entry.path, unique_dest, time.strftime("%Y-%m-%d %H:%M:%S")])

#process files in the source directory
for entry in os.scandir(source_dir):
    if entry.is_file() and not entry.name.startswith("."):
        name = entry.name.lower()
        size = entry.stat().st_size
         
        #audio and music files
        if name.endswith(('.mp3', '.wav', '.aac','.m4a')):
                if size < 2500000 or 'sfx' in name.upper():
                    move_files(entry, "audio")
                else:
                    move_files(entry, "music")
        
        #for vidoe files
        elif name.endswith(('.mp4', '.avi', '.mkv')):
                move_files(entry, "videos")
        
        #for image files
        elif name.endswith(('.jpg', '.jpeg', '.png', '.gif','.avif'))   :
                move_files(entry, "images")
        
        #for document files
        elif name.endswith(('.pdf', '.docx', '.txt', '.pptx'))   :
                move_files(entry, "documents")
        else:
                print(f"Skipped: {entry.name} (unsupported type)")

print("\n All files processed!")
print("Check the folders and file_log.csv for details.")