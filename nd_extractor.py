import os
import sys
import json
from tqdm import tqdm

def stream_ndjson_file(file_path):
    """
    Stream-process an ndjson file and yields the 'body' content of each item,
    ignoring items without a 'body' key or where 'body' is equal to "[deleted]".

    Parameters:
    - file_path (str): Path to the ndjson file to be read.

    Yields:
    - str: 'body' content from the ndjson file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                item = json.loads(line)
                if 'body' in item and item['body'] != "[deleted]":
                    yield item['body'].replace("\n", " ")
            except json.JSONDecodeError:
                pass

def scanner(dir_path):
    """
    Recursively searches for and accumulates all NDJSON file paths in a directory.

    Parameters:
    - dir_path (str): Directory path to begin search.

    Returns:
    - list: Paths to all ndjson files in the directory and sub-directories.
    """
    out_list = []
    obj = os.scandir(dir_path)
    for i in obj:
        if i.is_file() and i.name.lower().endswith('.ndjson'):
            out_list.append(i.path)
        elif i.is_dir():
            out_list.extend(scanner(i.path))
    return out_list

def main(input_directory, output):
    buffer = []
    buffer_limit = 10000  # Adjust as per available memory

    ndjson_files = scanner(input_directory)

    with open(output, 'w', encoding='utf-8') as f:
        for filepath in tqdm(ndjson_files, desc="Processing files", unit="file"):
            for text in stream_ndjson_file(filepath):
                buffer.append(text)
                if len(buffer) >= buffer_limit:
                    f.write('\n'.join(buffer) + '\n')
                    buffer.clear()

        if buffer:
            f.write('\n'.join(buffer) + '\n')

    print(f"Text data from NDJSON files saved to {output}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_directory> <output_file>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output = sys.argv[2]

    if not os.path.isdir(input_directory):
        print(f"'{input_directory}' is not a valid directory.")
        sys.exit(1)

    main(input_directory, output)
