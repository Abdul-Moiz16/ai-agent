
import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a specified file relative to the working directory, returning a success message or an error message",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to write to, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file",
                },
            },
        },
    },
}

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