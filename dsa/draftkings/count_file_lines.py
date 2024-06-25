def count_lines_in_file(path):
    line_count = 0
    with open(path, 'r') as file:
        for line in file:
            line_count += 1
    return line_count


file_path = 'dsa/draftkings/count_file_lines.py'
total_lines = count_lines_in_file(file_path)
print("Total number of lines:", total_lines)
