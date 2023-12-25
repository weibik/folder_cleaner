import os
import shutil

images = ["jpg", "png"]
documents = ["txt"]


def clean_folder(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for dirpath, dirnames, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(dirpath, file)

            _, file_extension = os.path.splitext(file)

            destination_path = os.path.join(destination_folder, file_extension.lower()[1:])

            if not os.path.exists(destination_path):
                os.makedirs(destination_path)

            # Move the file to the destination folder
            shutil.move(source_path, os.path.join(destination_path, file))