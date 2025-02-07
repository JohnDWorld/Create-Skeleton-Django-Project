"""
Django Project Generator from JSON File
----------------------------------------

Description:
This script automates the creation of a complete Django project based on a JSON file. 
The JSON file should include the necessary specifications, such as models, views, 
routes, and other configurations. The goal is to streamline and simplify the Django 
project creation process.

Author: Jonathan Demory
Society: The Van Codeur 
Email: j.demory@thevancodeur.com
Creation Date: 26 December 2024  
Version: 1.0  

How to Use:
1. Ensure Python 3.8 or later is installed on your system.  
2. Prepare a JSON file following the required format (see documentation for details).  
3. Run the script with the command: `python main.py`.  

Prerequisites:
- Python 3.8+
- JSON file (see documentation for details)

Warning:
- This script may overwrite existing files in the target folder. Back up your data before running it.  
- Verify the JSON file content to avoid errors or undesired configurations.  

Notes:
- The script is intended for local use only. Adaptations may be required for production deployment.  
- Feel free to report bugs or suggest improvements.  
"""

import os
import time

from constants import Constants
from utils import (
    check_files_dependencies,
    load_config,
    create_venv,
    slugify,
    update_settings,
    ask_user_rewrite,
)
from generate_project import (
    create_project,
    create_project_templates,
    add_static_folder_setting,
    create_urls_main_app,
)
from generate_application import generate_app

# Initialize the constants
constants = Constants()


def main():
    """Main function."""
    # Check if the necessary files and directories exist
    check_files_dependencies(constants.FILE_JSON_NAME, constants.TEMPLATES_DIR)

    # Load the configuration
    config = load_config(constants.FILE_JSON_NAME)

    # Creation of the virtual environment
    if not os.path.exists(constants.PATH_PYTHON):
        create_venv(config, constants)

    # Slugify the project name
    config["slug"] = slugify(constants.PATH_PYTHON, config["project"])

    # Add the project constants
    constants.add_project(config)

    # Creation of the Django project
    if not os.path.exists(constants.PRJ_DIR):
        create_project(config, constants)
        print(f"\nProject {config.get('project')} created successfully !\n")
        time.sleep(constants.SLEEP_TIME)
    else:
        constants.create_project = False

    update_settings(constants, config, "TEMPLATES")
    update_settings(constants, config, "MIDDLEWARE")
    add_static_folder_setting(config, constants)
    create_urls_main_app(config, constants)

    # Creation of the templates and static directories
    create_project_templates(config, constants)

    # Creation of the Django apps
    for app, value in config.get("apps").items():
        constants.add_app(app)
        if os.path.exists(constants.APP_DIR):
            constants.create_app = False
        # Generate the app
        if (
            constants.create_app
            or not constants.create_app
            and ask_user_rewrite(None, constants.SLUG_APP_NAME)
        ):
            generate_app(config, constants, value)
            if constants.create_app:
                print(
                    f"The application '{constants.SLUG_APP_NAME}' has been generated successfully !\n"
                )
            else:
                print(
                    f"The application '{constants.SLUG_APP_NAME}' has been updated successfully !\n"
                )
            time.sleep(constants.SLEEP_TIME)


if __name__ == "__main__":
    main()
