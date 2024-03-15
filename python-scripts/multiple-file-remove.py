#! /usr/bin/python3
import os


def removeDir():
    root_path = os.getcwd()
    file_name = '.htaccess'
    for roots, dirs, files in os.walk(root_path):
        if file_name in files:
            file_path = os.path.join(roots, file_name)
            if os.path.isfile(file_path) and file_path != os.path.join(root_path, file_name):
                print(f"removing {file_path} ...")
                os.remove(file_path)
                print(f"file Removed ...")


if __name__ == '__main__':
    removeDir()
