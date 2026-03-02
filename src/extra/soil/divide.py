import math
import os


def split_file_by_lines(filename, n, target_folder=None):
    """
    Splits a text file into n smaller files.
    """
    # 1. Determine the target directory
    if target_folder is None:
        target_folder = os.path.dirname(os.path.abspath(filename))

    # Create the folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 2. Read the lines from the source file
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    total_lines = len(lines)
    if total_lines == 0:
        print("The file is empty.")
        return

    # 3. Calculate lines per file (rounding up to cover all lines)
    lines_per_file = math.ceil(total_lines / n)

    # 4. Generate the files
    base_name = os.path.splitext(os.path.basename(filename))[0]

    for i in range(n):
        start_index = i * lines_per_file
        end_index = start_index + lines_per_file
        chunk = lines[start_index:end_index]

        # Avoid creating empty files if n > total_lines
        if not chunk:
            break

        output_filename = f"{base_name}_part_{i + 1}.txt"
        output_path = os.path.join(target_folder, output_filename)

        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.writelines(chunk)

    print(f"Successfully split {total_lines} lines into {n} files in: {target_folder}")


if __name__ == '__main__':
    # Example usage:
    split_file_by_lines('cleaned_transcript.txt', 3)
