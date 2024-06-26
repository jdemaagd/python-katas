"""
Time Complexity -> 𝑂(𝑛)
File Opening: open function call is typically 𝑂(1)
  as it does not depend on the file size but on the operating system's file management
Reading Lines: function iterates over each line in file -> operation is 𝑂(𝑛)
  because each iteration processes a line, and number of iterations is equal to number of lines
Counting Lines: for each line, `line_count += 1` operation is 𝑂(1) as incrementing an integer takes constant time
Therefore, total time complexity is dominated by line reading process, which is 𝑂(𝑛).

Space Complexity -> 𝑂(1)
Variable Storage: primary variable `line_count` is an integer, which takes 𝑂(1)
File Object: `file` object and iteration over it do not require additional space proportional to file size
  since file objects are typically iterated in buffered manner, consuming constant memory regardless of file size
Line Buffering: most file handling libraries read files line-by-line into a buffer, space for each line is 𝑂(𝑙),
  where 𝑙 is length of line, however, since this buffer is reused for each line, space complexity remains 𝑂(1)
  relative to file size or number of lines
"""


def count_lines_in_file(path):
    line_count = 0
    with open(path, 'r') as file:
        for line in file:
            line_count += 1
    return line_count


file_path = 'dsa/draftkings/count_file_lines.py'
total_lines = count_lines_in_file(file_path)
print("Total number of lines:", total_lines)
