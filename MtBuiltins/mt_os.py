import os


def return_all_files_in_dir_recursively(dir_path):
    files = []
    for d, _, fs in os.walk(dir_path):
        for tmp in fs:
            files.append(os.path.join(d, tmp))
    return files
