import os
import sys


def list_files(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            print(os.path.join(root, file))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_duplicate.py <folder>")
        sys.exit(1)

    folder = sys.argv[1]
    if not os.path.isdir(folder):
        print(f"The specified path is not a folder: {folder}")
        sys.exit(1)

    list_files(folder)
