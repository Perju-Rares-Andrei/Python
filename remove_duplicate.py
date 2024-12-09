import os
import sys
import filecmp

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

def find_duplicates_by_comparison(files_by_size):
    duplicates = []
    for size, files in files_by_size.items():
        if len(files) > 1:
            for i in range(len(files)):
                for j in range(i + 1, len(files)):
                    try:
                        if filecmp.cmp(files[i], files[j], shallow=False):
                            duplicates.append((files[i], files[j]))
                    except Exception as e:
                        print(f"Could not compare {files[i]} and {files[j]}: {e}")
    return duplicates
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


    duplicates = find_duplicates_by_comparison(files_by_size)
    print("Duplicate files:")
    for original, duplicate in duplicates:
        print(f"{original} == {duplicate}")