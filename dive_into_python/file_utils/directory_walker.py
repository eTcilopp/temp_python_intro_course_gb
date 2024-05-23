"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
- Для дочерних объектов указывайте родительскую директорию.
- Для каждого объекта укажите файл это или директория.
- Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""

import os
import json
import csv
import pickle

__all__ = ['directory_walker']


def directory_walker(directory: str):

    def get_size(path: str):
        if os.path.isfile(path):
            return os.path.getsize(path)
        if os.path.isdir(path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
            return total_size

    def get_files_and_dirs(path: str):
        files = []
        dirs = []
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                files.append({
                    "name": f,
                    "path": fp,
                    "size": os.path.getsize(fp)
                })
            for d in dirnames:
                dp = os.path.join(dirpath, d)
                dirs.append({
                    "name": d,
                    "path": dp,
                    "size": get_size(dp)
                })
        return files, dirs

    def save_to_json(data: dict, filename: str):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def save_to_csv(data: list[dict], filename: str):
        with open(filename, 'w', newline='') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(data[0].keys())
            for row in data:
                csvwriter.writerow(row.values())

    def save_to_pickle(data: dict, filename: str):
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

    files, dirs = get_files_and_dirs(directory)
    data = {
        "files": files,
        "dirs": dirs
    }

    save_to_json(data, 'files_and_dirs.json')
    save_to_csv(files + dirs, 'files_and_dirs.csv')
    save_to_pickle(data, 'files_and_dirs.pickle')


directory_walker('dive_into_python')
if __name__ == '__main__':
    directory_walker('dive_into_python')
