import os
import shutil
import pathlib

SRC_PATH = './scala-tutorial/source'
name_list = ['car','test']

files = os.listdir(SRC_PATH)
for f in files:
    for names in name_list:
        if names in f:
            created_folder = os.path.join(SRC_PATH, names)
            filepath = os.path.join(SRC_PATH, f)
            os.makedirs(created_folder, exist_ok=True)
            shutil.move(filepath, created_folder)