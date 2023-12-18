import os
import shutil
import pathlib
import re


def sanitize_folder_name(name):
    # Replace spaces and unwanted characters with underscores
    sanitized = re.sub(r"[^\w\-_\.]", "_", name)
    # Remove trailing special characters like '!'
    sanitized = re.sub(r"[_!@#$%^&*()+=]+$", "", sanitized)
    return sanitized


def unzip(zip_name, modpack_name, file_ext, this_dir, output=False):
    if output:
        folder_name = sanitize_folder_name(output)
    else:
        folder_name = sanitize_folder_name(modpack_name)

    extract_dir = os.path.join(this_dir, folder_name)
    my_zip = os.path.join(this_dir, zip_name)
    shutil.unpack_archive(my_zip, extract_dir)
    print("Extraction Done, deleting zip")
    os.remove(my_zip)
    # oschmod.set_mode_recursive(extract_dir, "777")
    path = pathlib.PurePath(extract_dir)
    return path.name
