
import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_directory = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(working_directory, file_path))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_directory, target_directory]) == working_directory
    try:
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_directory):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        with open(target_directory, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'