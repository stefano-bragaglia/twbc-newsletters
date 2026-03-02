import re


def clean_transcript(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 1. Extract the title (first non-empty line)
    title = ""
    content_start_index = 0

    for i, line in enumerate(lines):
        clean_line = line.strip()
        if clean_line:
            title = clean_line
            content_start_index = i + 1
            break

    # 2. Process the remaining lines
    # Pattern matches 0:00, 10:00, or 1:00:00 (hh:mm:ss)
    timestamp_pattern = re.compile(r'^\d{1,2}:\d{2}(:\d{2})?$')

    cleaned_content = []
    for line in lines[content_start_index:]:
        text = line.strip()

        # Skip empty lines or lines that match the timestamp format
        if not text or timestamp_pattern.match(text):
            continue

        cleaned_content.append(text)

    # 3. Save to new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{title}\n\n")
        # Join lines with a space or newline depending on your preference
        f.write("\n".join(cleaned_content))

if __name__ == '__main__':
    # Usage
    clean_transcript(
        'transcript.txt',
        'cleaned_transcript.txt')