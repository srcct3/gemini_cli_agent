import os
from config import MAX_CHAR


def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))

    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    file_info_string = lambda x: f'- {x.split("/")[-1]}: file_size={os.path.getsize(x)} bytes, is_dir={os.path.isdir(x)}'
    try:
        res = map(lambda x: file_info_string(
            os.path.join(target_dir, x)), os.listdir(target_dir))
        return "\n".join(list(res))
    except Exception as e:
        return f'Error: {e}'


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHAR)
            if len(file_content_string) == MAX_CHAR:
                file_content_string += f'[...File "{
                    file_path}" truncated at 10000 characters]'
            return file_content_string

    except Exception as e:
        return f"Error: {e}"

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        target_dir = os.path.dirname(target_file)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        with open(target_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'
