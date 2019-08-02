import os
import sys
import shutil
from pathlib import Path

if len(sys.argv) >= 2:
    os.chdir(sys.argv[1])
else:
    print("Filepath must be provided as Argument")
    exit()

_files = os.listdir(os.getcwd())
_duplicateFolderName = "Duplicates"


def move_file(file_name, folder_name):
    shutil.move(str(file_name), folder_name)


def create_duplicate_folder():
    if not os.path.exists(os.path.join(os.getcwd(), _duplicateFolderName)):
        os.mkdir(os.path.join(os.getcwd(), _duplicateFolderName))


def files_are_equal(path_to_first_file, size_of_first_file, path_to_second_file):
    if path_to_second_file.exists():
        _size_second_file = os.path.getsize(path_to_second_file)
        return size_of_first_file == _size_second_file
    else:
        return False


for i in range(len(_files)):
    _duplicateFound = False
    _pathFirstFile = Path(os.path.join(os.getcwd(), _files[i]))
    if _pathFirstFile.exists():
        _sizeFirstFile = os.path.getsize(os.path.join(os.getcwd(), _files[i]))
        for j in range(i + 1, len(_files)):
            _pathSecondFile = Path(os.path.join(os.getcwd(), _files[j]))
            if files_are_equal(_pathFirstFile, _sizeFirstFile, _pathSecondFile):
                _duplicateFound = True
                create_duplicate_folder()
                move_file(_pathSecondFile, _duplicateFolderName)

        if _duplicateFound:
            move_file(_pathFirstFile, _duplicateFolderName)
