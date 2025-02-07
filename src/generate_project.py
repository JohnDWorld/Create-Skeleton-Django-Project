import os
import subprocess

from utils import ask_user_rewrite


def create_project(config, constants):
    """Create the Django project"""
    project_name = config.get("project")
    os.chdir(constants.PROJECTS_DIR)

    # Create the Django project
    subprocess.run(
        [constants.PATH_PYTHON, "-m", "django", "startproject", config.get("slug")],
        check=True,
    )

    # Rename the project directory with the project name
    os.rename(config.get("slug"), project_name)


def create_project_templates(config, constants):
    """Create the templates directory for the project."""
    # Create the templates and static directory
    if not os.path.exists(constants.PRJ_DIR_TEMPLATES):
        os.mkdir(constants.PRJ_DIR_TEMPLATES)
    if not os.path.exists(constants.PRJ_DIR_STATIC):
        os.mkdir(constants.PRJ_DIR_STATIC)

    # Create the templates base.html file
    if (
        constants.create_project
        or not constants.create_project
        and ask_user_rewrite(constants.KEYWORD_HTML_BASE, config.get("project"))
    ):
        settings = config.get("settings")
        lg_html = settings.get("language_html")
        with open(constants.FILE_HTML_BASE, "r") as f:
            with open(
                constants.MAIN_APP_FILE_HTML_BASE,
                "w",
            ) as f2:
                for line in f:
                    # Check if the line contains the bootstrap link and script or the language
                    if (
                        constants.PATTERN_LANGUAGE_HTML not in line
                        and constants.PATTERN_BOOTSTRAP_LINK not in line
                        and constants.PATTERN_BOOTSTRAP_SCRIPT not in line
                    ):
                        f2.write(line)
                    else:
                        # Replace the language
                        if constants.PATTERN_LANGUAGE_HTML in line:
                            line = line.replace(
                                constants.PATTERN_LANGUAGE_HTML, lg_html
                            )
                            f2.write(line)
                        # Replace the bootstrap link and script
                        elif (
                            config.get("bootstrap")
                            and constants.PATTERN_BOOTSTRAP_LINK in line
                        ):
                            line = line.replace(
                                constants.PATTERN_BOOTSTRAP_LINK,
                                constants.BALISE_BOOTSTRAP_LINK,
                            )
                            f2.write(line)
                        elif (
                            config.get("bootstrap")
                            and constants.PATTERN_BOOTSTRAP_SCRIPT in line
                        ):
                            line = line.replace(
                                constants.PATTERN_BOOTSTRAP_SCRIPT,
                                constants.BALISE_BOOTSTRAP_SCRIPT,
                            )
                            f2.write(line)
                        else:
                            pass

    # Create the templates 404.html file
    if (
        constants.create_project
        or not constants.create_project
        and ask_user_rewrite(constants.KEYWORD_HTML_ERROR, config.get("project"))
    ):
        with open(constants.FILE_HTML_ERROR, "r") as f:
            with open(
                constants.MAIN_APP_FILE_HTML_ERROR,
                "w",
            ) as f2:
                f2.write(f.read())

    # Create the app.css file
    if (
        constants.create_project
        or not constants.create_project
        and ask_user_rewrite(constants.KEYWORD_CSS_APP, config.get("project"))
    ):
        with open(constants.MAIN_APP_FILE_CSS_APP, "w") as f:
            f.write("/* Add your CSS styles here */")

    # Create the uploads folder
    if config.get("uploads") and not os.path.exists(
        os.path.join(constants.PRJ_DIR, "uploads")
    ):
        os.mkdir(os.path.join(constants.PRJ_DIR, "uploads"))


def add_static_folder_setting(config, constants):
    """Add the STATIC and MEDIA setting to the settings.py file."""
    lines_to_add = [
        'STATIC_URL = "/static/"',
        'STATIC_ROOT = BASE_DIR / "staticfiles"',
        'STATICFILES_DIRS = [BASE_DIR / "static"]\n',
    ]
    if config.get("uploads"):
        lines_to_add.append('MEDIA_ROOT = BASE_DIR / "uploads"')
        lines_to_add.append('MEDIA_URL = "/files/"')
    # Get the lines from the file
    with open(constants.MAIN_APP_FILE_SETTINGS, "r") as file:
        lines = file.readlines()

    # Find  the line where add the new line
    with open(constants.MAIN_APP_FILE_SETTINGS, "w") as file:
        for i in range(len(lines)):
            if lines[i].startswith("STATIC_URL =") and lines[i + 1] == "\n":
                # Ajouter les nouvelles lignes juste après
                for new_line in lines_to_add:
                    file.write(new_line + "\n")
            else:
                file.write(lines[i])


def create_urls_main_app(config, constants):
    """Create the urls.py for the main application."""
    if (
        constants.create_project
        or not constants.create_project
        and ask_user_rewrite(constants.KEYWORD_PYTHON_URLS, config.get("project"))
    ):
        with open(constants.MAIN_APP_FILE_URLS_MAIN, "r") as f:
            line_content = f.readlines()
            with open(
                constants.MAIN_APP_FILE_URLS,
                "w",
            ) as f2:
                for line in line_content:
                    f2.write(line)
                    if "]" in line and config.get("uploads"):
                        f2.write(
                            "    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n"
                        )
