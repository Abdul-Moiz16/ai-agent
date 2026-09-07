import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_directory = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(working_directory, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_directory, target_directory]) == working_directory
    try:
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if directory != ".":
            return f'Error: "{directory}" is not a directory'
        if valid_target_dir:
            return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f'Error: {str(e)}'