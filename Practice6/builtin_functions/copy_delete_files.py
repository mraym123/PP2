import os
import shutil

# Copy file first (if it exists) before deleting
if os.path.exists("example.txt"):
    shutil.copy("example.txt", "backup_example.txt")  # Make a backup copy
    os.remove("example.txt")                          # Delete original file
    print("File backed up and deleted")
else:
    print("File does not exist")


# Import the os module to work with the operating system (check files, delete files, etc.)
import os

# Check if the file "example.txt" exists
if os.path.exists("example.txt"):
    # If the file exists, delete it
    os.remove("example.txt")
    print("File is deleted")  # Confirmation message
else:
    # If the file does not exist, print a message
    print("File does not exist")