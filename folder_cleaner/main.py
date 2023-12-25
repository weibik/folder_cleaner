from folder_cleaner.struct import clean_folder

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")

    clean_folder(source_folder, destination_folder)

    print("Folder cleaning completed.")
