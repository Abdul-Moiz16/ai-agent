import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    files_list = []
    working_directory = os.path.abspath(working_directory)
    target_directory = os.path.normpath(os.path.join(working_directory, directory))
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_directory, target_directory]) == working_directory
    try:
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if os.path.isdir(target_directory) is False:
            return f'Error: "{directory}" is not a directory'
        
        item_in_directory = os.listdir(target_directory)
        
        for item in item_in_directory:
            if os.path.isdir(os.path.join(target_directory, item)):
                is_dir = True
            else:
                is_dir = False
            file_size = os.path.getsize(os.path.join(target_directory, item))
            files_list.append(f'- {item}: file_size={file_size} bytes, is_dir={is_dir}')
        return "\n".join(files_list)

    except Exception as e:
        return f'Error: {str(e)}'