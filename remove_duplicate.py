import os
import sys


def list_files(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            print(os.path.join(root, file))

def group_files_by_size(folder):
    files_by_size = {}
    for root, _, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                files_by_size.setdefault(file_size, []).append(file_path)
            except Exception as e:
                print(f"Could not process file {file_path}: {e}")
    return files_by_size


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicate.py <folder>")
        sys.exit(1)

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"The specified path is not a folder: {folder}")
        sys.exit(1)

    list_files(folder)

    files_by_size = group_files_by_size(folder)
    for size, files in files_by_size.items():
        print(f"Size: {size} bytes -> Files: {files}")