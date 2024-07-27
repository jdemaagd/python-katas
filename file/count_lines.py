import os
from heapq import nlargest


def count_lines_in_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
        return sum(1 for _ in file)


def find_top_ten_files_with_most_lines(root_dir, file_extension=".kt"):
    file_lines = []

    for subdir, _, files in os.walk(root_dir):
        for f in files:
            if f.endswith(file_extension):
                file_path = os.path.join(subdir, f)
                try:
                    line_count = count_lines_in_file(file_path)
                    file_lines.append((line_count, file_path))
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")

    top_ten_files = nlargest(10, file_lines, key=lambda x: x[0])
    return top_ten_files


if __name__ == "__main__":
    project_dir = input("Enter the path to your Android project: ").strip()
    result = find_top_ten_files_with_most_lines(project_dir)
    if result:
        print("Top ten kotlin files with most lines:")
        for lines, file in result:
            print(f"{file}: {lines} lines")
    else:
        print("No kotlin files found in the directory")
