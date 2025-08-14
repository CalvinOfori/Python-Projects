import os
import shutil

Directories = {
    "Images": ["jpeg", "jpg", "png"],
    "Videos": ["avi", "mov", "mp4"],
    "Document": ["pdf", "docx", "doc"],
    "Music": ["mp3", "m4a"],
    "Others": [] 
}

source_dir = input("Enter the path of the directory to organize: ")

# Create category subdirectories if they don't exist
for folder_name in Directories:
    folder_path = os.path.join(source_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Also create the 'Others' directory explicitly
others_path = os.path.join(source_dir, "Others")
os.makedirs(others_path, exist_ok=True)

for filename in os.listdir(source_dir):
    filepath = os.path.join(source_dir, filename)

    # Skip if it's a directory (or one of our newly created category folders)
    if os.path.isdir(filepath):
        # Check if the directory is one of our created categories
        if filename in Directories.keys() or filename == "Others":
            continue # Skip our own created directories
        # If it's a subdirectory, we can choose to handle it differently if needed
        else:
            continue # Skip any other subdirectories

    if os.path.isfile(filepath):
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False

        # Try to move to a specific category
        for category, extensions in Directories.items():
            # Check if the file_extension (without leading dot) is in the current category's extensions
            if file_extension and file_extension[1:] in extensions:
                destination_folder = os.path.join(source_dir, category)
                destination_filepath = os.path.join(destination_folder, filename)

                if not os.path.exists(destination_filepath):
                    shutil.move(filepath, destination_folder)
                    print(f"Moved '{filename}' to {category}")
                else:
                    print(f"Skipped '{filename}': Already exists in '{category}/'")
                moved = True # Mark as handled whether moved or skipped
                break # Exit the inner loop once a category is found/handled

        # If not moved to a specific category and has an extension, try to move to 'Others'
        if not moved and file_extension:
            destination_folder = os.path.join(source_dir, "Others")
            destination_filepath = os.path.join(destination_folder, filename)

            if not os.path.exists(destination_filepath):
                shutil.move(filepath, destination_folder)
                print(f"Moved '{filename}' to Others")
            else:
                print(f"Skipped '{filename}': Already exists in 'Others/'.")

