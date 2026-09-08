
import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    working_directory = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(working_directory, file_path))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_directory, target_directory]) == working_directory
    try:
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if os.path.isfile(target_directory) is False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if file_path.endswith(".py") is False:
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_directory] + (args or [])
        output = ""
        completed_process = subprocess.run(command, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=working_directory, timeout=30, check=False, encoding=None, errors=None, text=True, env=None, universal_newlines=None)
        if completed_process.returncode != 0:
            output += f"Process exited with code {completed_process.returncode}\n"
        if completed_process.stdout and completed_process.stdout == "":
            output += f"No output produced"
        else:
            output += f"STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}"
        return output
    except Exception as e:
        return f'Error: {str(e)}'