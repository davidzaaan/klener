# Life-purpose Script: Delete every downloaded file when executed

# Error codes:
# 101 - Directory is empty
# 105 - Some file is still being used thus cannot be deleted
# 0 - Success deleting all files

import os

PATH: str = f"C:/Users/{os.environ.get('USERNAME')}/Downloads/"

def main() -> None:
    op_code: int = delete_files(PATH)

    if op_code == 0:
        print("Files deleted successfully")
    elif op_code == 101:
        print("Directory is currently empty")
    elif op_code == 105:
        print("Error: files are still being used")


def delete_files(downloads_folder: str) -> None:
    """
        Function that deletes all the downloaded files when called
        :param downloads_folder: The path that cointains all the downloaded files
        :return int: Numeric code with the operation result
    """
    # Getting all the current downloaded files
    files: list = os.listdir(downloads_folder)

    if not len(files) > 1:
        return 101

    for filename in files:
        # .ini files are not recommended to delete because
        # they contain information about how the folder is displayed to the user
        if not filename.endswith('.ini'):
            try:
                os.remove(PATH + filename)
            except:
                return 105
    
    return 0


if __name__ == '__main__':
    main()