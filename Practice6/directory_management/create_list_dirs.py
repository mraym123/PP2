import os  # Import the os module to interact with the operating system (create folders, list files, etc.)

# Create nested directories: my_folder → sub_folder → inner_folder
# exist_ok=True ensures no error occurs if the folders already exist
os.makedirs("my_folder/sub_folder/inner_folder", exist_ok=True)

print("Папкалар сәтті құрылды")  # Print confirmation that folders were created successfully

# Define the path to the folder we want to inspect
path = "my_folder"

# List all items (files and folders) in the specified path
items = os.listdir(path)

# Loop through each item in the folder and print its name
for item in items:
    print(item)