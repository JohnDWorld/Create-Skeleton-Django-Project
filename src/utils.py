import os
import json
import subprocess
import time
import ast


def _update_pip_version(constants):
    subprocess.run(
        [constants.PATH_PYTHON, "-m", "pip", "install", "--upgrade", "pip"],
        check=True,
    )


def check_files_dependencies(json_file, templates_dir):
    """Check if the necessary files and directories exist."""
    if not os.path.exists(json_file):
        raise FileNotFoundError(f"The file JSON '{json_file}' was not found.")
    if not os.path.exists(templates_dir):
        raise FileNotFoundError("The directory templates was not found.")


def load_config(file_path):
    """Load the configuration from the JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_venv(config, constants):
    """Create the virtual environment and install dependencies."""
    os.chdir(constants.SRC_DIR)
    os.system("python -m venv venv")
    dependencies = ["django", "pillow", "python-slugify"] + config.get("dependencies")
    _update_pip_version(constants)
    for dependency in dependencies:
        subprocess.run(
            [constants.PATH_PYTHON, "-m", "pip", "install", dependency],
            check=True,
        )
    print(f"\nVirtual environment created and dependencies installed successfully!\n")
    time.sleep(constants.SLEEP_TIME)


def check_dependencies(config, constants):
    """Check if the dependencies are installed and update pip."""
    dependencies = config.get("dependencies")
    _update_pip_version(constants)
    pip_list = subprocess.run(
        [constants.PATH_PYTHON, "-m", "pip", "list"],
        stdout=subprocess.PIPE,
        text=True,
        check=True,
    )
    for dependency in dependencies:
        if dependency not in pip_list.stdout:
            subprocess.run(
                [constants.PATH_PYTHON, "-m", "pip", "install", dependency],
                check=True,
            )
    print(
        f"\nVirtual environment updated with new dependencies and updates pip successfully!\n"
    )
    time.sleep(constants.SLEEP_TIME)


def slugify(PATH_PYTHON, name):
    """Create a slug from the project name."""
    result = subprocess.run(
        [
            PATH_PYTHON,
            "-c",
            f'from slugify import slugify; print(slugify("{name}", separator="_"))',
        ],
        stdout=subprocess.PIPE,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def ask_user_rewrite(file, app_name):
    """Ask the user if he wants to rewrite the file."""
    if file:
        answer = input(
            f"\nDo you want to rewrite the file {file} in {app_name} ? (N/y): \n"
        ).lower()
    else:
        answer = input(
            f"\nDo you want to rewrite some files in the application {app_name} ? (N/y): \n"
        ).lower()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("Answer with 'n/N' or 'y/Y' please.")
        return ask_user_rewrite(file, app_name)


def update_settings(constants, config, name_list):
    """Update settings.py."""
    with open(constants.MAIN_APP_FILE_SETTINGS, "r") as f:
        content = f.read()

    # Find and extract list
    start = content.find(f"{name_list} =")
    if start == -1:
        raise ValueError(f"{name_list} not found in settings.py.")

    if name_list == "TEMPLATES":
        with open(constants.MAIN_APP_FILE_SETTINGS, "r") as f:
            lines = f.readlines()

        # Add the new value
        with open(constants.MAIN_APP_FILE_SETTINGS, "w") as f:
            for line in lines:
                if "'DIRS': []," in line:
                    line = '        "DIRS": [ BASE_DIR / "templates"],\n'
                f.write(line)
    else:
        # Extract the list
        start += len(f"{name_list} =")
        end = content.find("]", start) + len("]")
        list_str = content[start:end].strip()

        list_to_update = ast.literal_eval(list_str)

        # Add the new value to the list
        match name_list:
            case "MIDDLEWARE":
                if (
                    constants.MIDDLEWARE not in list_to_update
                    and config.get("settings").get("language_html").lower() != "en"
                ):
                    list_to_update.append(constants.MIDDLEWARE)
            case "INSTALLED_APPS":
                if constants.SLUG_APP_NAME not in list_to_update:
                    list_to_update.append(constants.SLUG_APP_NAME)

        # Rebuild the list as a string
        updated_list_str = f"{list_to_update}"
        updated_content = content[:start] + " " + updated_list_str + content[end:]

        # Rewrite the file settings.py
        with open(constants.MAIN_APP_FILE_SETTINGS, "w") as f:
            f.write(updated_content)


def install_reactjs(constants):
    pass
