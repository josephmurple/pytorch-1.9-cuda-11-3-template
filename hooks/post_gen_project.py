import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{ cookiecutter.package_management }}" == "pip":
    file_to_delete = os.path.join(os.getcwd(), "pyproject.toml")
    print(f"[getcwd]: {os.getcwd()}")
    print(f"[file to delete]: {file_to_delete}")
    remove(file_to_delete)
elif "{{ cookiecutter.package_management }}" == "poetry":
    file_to_delete = os.path.join(os.getcwd(), "requirements")
    print(f"[getcwd]: {os.getcwd()}")
    print(f"[file to delete]: {file_to_delete}")
    remove(file_to_delete)

print("Done!! Now, you can develop FastAPI project!!")
