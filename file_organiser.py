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
    folder_path = os.path.join(FOLDER_PATH, folder) 
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

