import os
import hashlib

from domain.FileInfo import FileInfo


file_list = []


def get_files_list(current_directory):
    files = os.listdir(current_directory)
    for file in files:
        path = os.path.join(current_directory, file)
        if os.path.isfile(path):
            file_list.append(path)
        else:
            get_files_list(path)
    return file_list


def calculate_hash(file_path):
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def get_file_info(file_path):
    hash = calculate_hash(file_path)
    size = os.path.getsize(file_path)
    info = FileInfo(size, file_path, hash)
    # print(f"{info.path}\t {info.size}\t {info.hash}")
    return info


def find_files(dir):
    results = []
    get_files_list(dir)
    for file in file_list:
        info = get_file_info(file)
        results.append(info)
    return results
