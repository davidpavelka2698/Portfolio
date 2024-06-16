import os
import fileinput
import sys


def replace_in_files(directory, old_text, new_text):
    # Walk through all files and directories starting from 'directory'
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.html'):
                filepath = os.path.join(dirpath, filename)
                replace_in_file(filepath, old_text, new_text)


def replace_in_file(filepath, old_text, new_text):
    # Replace 'old_text' with 'new_text' in the specified file
    with fileinput.FileInput(filepath, inplace=True) as file:
        for line in file:
            sys.stdout.write(line.replace(old_text, new_text))


if __name__ == '__main__':
    directory = 'templates'  # Specify the directory where your HTML files are located
    old_text = '<li><a href="http://127.0.0.1:5001/">Back</a></li>'
    new_text = '<li><a href="../index.html">Back</a></li>'

    replace_in_files(directory, old_text, new_text)
