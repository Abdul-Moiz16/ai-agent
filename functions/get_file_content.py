import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    working_directory = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(working_directory, file_path))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_directory, target_directory]) == working_directory
    try:
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_directory) is False:
            return f'Error: "{file_path}" is not a file'

        with open(target_directory, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                return file_content_string
            else:
                return file_content_string
    except Exception as e:
        return f'Error: {str(e)}'
