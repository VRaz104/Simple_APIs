import os
import shutil
directory = os.path.join(os.path.expanduser("~"), "Desktop")
extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"]
}
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()
        category_found = False
        for category, ext_list in extensions.items():
            if extension in ext_list:
                category_found = True
                folder_path = os.path.join(directory, category)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} to {category}/")
                break
        if not category_found:
            print(f"Skipped: {filename} (unknown file type)")
    else:
        print(f"Skipped: {filename} (directory)")
print("File organization complete!")