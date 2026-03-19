import os
import shutil

# -----------------------------
# 1️⃣ Define folders
# -----------------------------
source_folder = "my_folder"       # Folder where the files currently are
destination_folder = "archive"    # Folder where we want to move the files

# Create destination folder if it does not exist
# exist_ok=True prevents an error if the folder already exists
os.makedirs(destination_folder, exist_ok=True)

# -----------------------------
# 2️⃣ Find all files in source folder
# -----------------------------
# os.walk goes through the folder and all its subfolders
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # Build full file path
        src_path = os.path.join(root, file)
        dest_path = os.path.join(destination_folder, file)
        
        # -----------------------------
        # 3️⃣ Move the file
        # -----------------------------
        shutil.move(src_path, dest_path)
        print(f"Moved file: {file} → {destination_folder}")

# -----------------------------
# 4️⃣ List files in the destination folder
# -----------------------------
print("\nAll files have been moved!")
print("Files now in the destination folder:")
for f in os.listdir(destination_folder):
    print(f)