import os
import shutil

FOLDER_PATH = os.getcwd()

# file type mapping
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Video': ['.mp4', '.avi', '.mkv', '.mov'],
    'archives': ['.zip', '.rar', '.tar', '.gz'],
    'scripts': ['.js', '.html', '.css']
}

# create folders if they don't exist
for folder in FILE_TYPES.keys():  # creating folders for each file type
    folder_path = os.path.join(FOLDER_PATH, folder)    # creating the path for the folder


    if not os.path.exists(folder_path):  # checking if the folder already exists


        os.makedirs(folder_path) # creating the folder if it doesn't exist

# organize files
for file in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file)

    #skip folders
    if os.path.isdir(file_path):
        continue
    # get file extension
    file_ext = os.path.splitext(file)[1].lower()

    for folder, extensions in FILE_TYPES.items():
        if file_ext in extensions:
            shutil.move(file_path, os.path.join(FOLDER_PATH, folder, file))

print("Files organized successfully!")
