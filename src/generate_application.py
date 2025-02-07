import os
import types

from utils import ask_user_rewrite, update_settings


def _get_arguments(constants, field):
    """Get the arguments in function of the filed."""
    for attr in dir(constants):
        value = getattr(constants, attr)
        if (
            not isinstance(value, types.MethodType)
            and not attr.startswith("__")
            and attr == field.upper()
            and isinstance(value, dict)
        ):
            return value[field]
    return ""


def _get_class_to_import(model_dict, keyword, constants):
    """Get the classes to import."""
    class_list = []
    if keyword == constants.KEYWORD_PYTHON_FORMS:
        class_list = [
            class_name
            for class_name, class_args in model_dict.items()
            if class_args.get("form")
        ]
    elif keyword == constants.KEYWORD_PYTHON_ADMIN:
        class_list = [
            class_name
            for class_name, class_args in model_dict.items()
            if class_args.get("admin").get("register")
        ]

    return f"from .models import {', '.join(class_list)}\n\n"


def _create_app(constants):
    """Create an application if it doesn't exist."""
    os.chdir(constants.PRJ_DIR)
    os.system(f'"{constants.PATH_PYTHON}" -m django startapp {constants.SLUG_APP_NAME}')


def _generate_app_templates_static(web_dict, constants):
    """Generate templates and static directories for an application."""
    os.makedirs(constants.APP_DIR_TEMPLATES, exist_ok=True)
    os.makedirs(constants.APP_DIR_STATIC, exist_ok=True)

    # Create the templates homepage.html file for app if it doesn't exist
    if (
        web_dict.get(constants.KEYWORD_TEMPLATES)
        and constants.create_app
        or web_dict.get(constants.KEYWORD_TEMPLATES)
        and not constants.create_app
        and ask_user_rewrite(constants.KEYWORD_HTML_HOMEPAGE, constants.SLUG_APP_NAME)
    ):
        with open(constants.FILE_HTML_HOMEPAGE, "r") as f:
            with open(
                constants.APP_DIR_TEMPLATES / constants.KEYWORD_HTML_HOMEPAGE,
                "w",
                encoding="utf-8",
            ) as f2:
                for line in f:
                    if constants.PATTERN_APP_NAME in line:
                        f2.write(
                            line.replace(
                                constants.PATTERN_APP_NAME, constants.SLUG_APP_NAME
                            )
                        )
                    else:
                        f2.write(line)

    # Create the static style.css file for app if it doesn't exist
    if (
        web_dict.get(constants.KEYWORD_STATIC)
        and constants.create_app
        or web_dict.get(constants.KEYWORD_STATIC)
        and not constants.create_app
        and ask_user_rewrite(constants.KEYWORD_CSS_STYLE, constants.SLUG_APP_NAME)
    ):
        with open(
            constants.APP_DIR_STATIC / constants.KEYWORD_CSS_STYLE,
            "w",
            encoding="utf-8",
        ) as f:
            f.write("/* Add your CSS styles here */")


def _generate_views(constants):
    """Generate views.py for an application."""
    if (
        constants.create_app
        or not constants.create_app
        and ask_user_rewrite(constants.KEYWORD_PYTHON_VIEWS, constants.SLUG_APP_NAME)
    ):
        with open(constants.FILE_PYTHON_VIEWS, "r") as f:
            with open(
                constants.APP_FILE_VIEWS,
                "w",
                encoding="utf-8",
            ) as f2:
                for line in f:
                    if constants.PATTERN_APP_NAME in line:
                        f2.write(
                            line.replace(
                                constants.PATTERN_APP_NAME, constants.SLUG_APP_NAME
                            )
                        )
                    else:
                        f2.write(line)


def _update_main_app_urls(constants):
    """Update urls.py of main application."""
    with open(constants.MAIN_APP_FILE_URLS, "r") as f:
        lines = f.readlines()

    # Add the new value
    with open(constants.MAIN_APP_FILE_URLS, "w") as f:
        for line in lines:
            if 'path("admin/", admin.site.urls)' in line:
                f.write(line)
                f.write(
                    f"        path('{constants.SLUG_APP_NAME}/', include('{constants.SLUG_APP_NAME}.urls')),\n"
                )
            else:
                f.write(line)


def _generate_urls(constants):
    """Generate views.py for an application."""
    if (
        constants.create_app
        or not constants.create_app
        and ask_user_rewrite(constants.KEYWORD_PYTHON_URLS, constants.SLUG_APP_NAME)
    ):
        with open(constants.FILE_PYTHON_URLS, "r") as f:
            with open(
                constants.APP_FILE_URLS,
                "w",
                encoding="utf-8",
            ) as f2:
                for line in f:
                    if constants.PATTERN_APP_NAME in line:
                        f2.write(
                            line.replace(
                                constants.PATTERN_APP_NAME, constants.SLUG_APP_NAME
                            )
                        )
                    else:
                        f2.write(line)


def _generate_model(model_dict, constants):
    """Generate models.py for an application."""
    if (
        constants.create_app
        or not constants.create_app
        and ask_user_rewrite(constants.KEYWORD_PYTHON_MODELS, constants.SLUG_APP_NAME)
    ):
        with open(constants.APP_FILE_MODELS, "w", encoding="utf-8") as f:
            # Prepare the file
            f.write("from django.db import models\n\n")
            f.write("# Create your models here.\n")
            # Walk through the models config
            for class_name, class_args in model_dict.items():
                f.write(f"class {class_name}(models.Model):\n")
                # Walk through the fields
                for arg_name, arg_value in class_args.items():
                    if arg_name == "admin" or arg_name == "form":
                        pass
                    elif isinstance(arg_value, dict) and arg_value.get("relation"):
                        # Gestion des relations
                        relation = arg_value["relation"]
                        to = arg_value["to"]
                        on_delete = arg_value["on_delete"]
                        line = f"    {arg_name} = models.{relation}('{to}', on_delete=models.{on_delete}"
                        line += ", null=True )\n" if on_delete == "SET_NULL" else ")\n"
                        f.write(line)
                    else:
                        # Gestion des autres champs
                        arg = _get_arguments(constants, arg_value)
                        f.write(f"    {arg_name} = models.{arg_value}({arg})\n")
                f.write("\n\n")


def _generate_form(model_dict, constants):
    """Generate forms.py for an application if forms is true in the model."""
    if (
        constants.create_app
        or not constants.create_app
        and ask_user_rewrite(constants.KEYWORD_PYTHON_FORMS, constants.SLUG_APP_NAME)
    ):
        # Create the forms.py file
        with open(constants.APP_FILE_FORMS, "w", encoding="utf-8") as f:
            # Prepare the file
            f.write("from django import forms\n\n")
            f.write(
                _get_class_to_import(
                    model_dict, constants.KEYWORD_PYTHON_FORMS, constants
                )
            )
            f.write("# Create your forms here.\n")
            # Walk through the models config
            for class_name, class_args in model_dict.items():
                if class_args.get("form"):
                    f.write(f"class {class_name}Form(forms.ModelForm):\n")
                    f.write("    class Meta:\n")
                    f.write(f"        model = {class_name}\n")
                    f.write("        fields = '__all__'\n")
                    f.write("        # exclude = []\n")
                    f.write("        # labels = {}\n")
                    f.write("        # error_messages = {}\n\n")


def _generate_admin(model_dict, constants):
    """Generate admin.py for an application."""
    if (
        constants.create_app
        or not constants.create_app
        and ask_user_rewrite(constants.KEYWORD_PYTHON_ADMIN, constants.SLUG_APP_NAME)
    ):
        list_register = []
        with open(constants.APP_FILE_ADMIN, "w", encoding="utf-8") as f:
            # Prepare the file
            f.write("from django.contrib import admin\n\n")
            f.write(
                _get_class_to_import(
                    model_dict, constants.KEYWORD_PYTHON_ADMIN, constants
                )
            )
            f.write("# Register your models here.\n")
            # Walk through the models config
            for class_name, class_args in model_dict.items():
                admin_args = class_args.get("admin")
                if admin_args.get("register"):
                    list_register.append("admin.site.register(" + class_name)
                    if len(admin_args) > 1:
                        class_name_admin = f"{class_name}Admin"
                        f.write(f"class {class_name_admin}(admin.ModelAdmin):\n")
                        for arg_name, arg_value in admin_args.items():
                            if arg_name != "register":
                                f.write(f"    {arg_name} = {arg_value}\n")
                        f.write("\n")
                        list_register[-1] += ", " + class_name_admin
                    list_register[-1] += ")\n"
            for line in list_register:
                f.write(line)


def generate_app(config, constants, app_config):
    for _, model_config in app_config.get(constants.KEYWORD_PYTHON_MODELS[:-3]).items():
        if model_config.get(constants.KEYWORD_PYTHON_FORMS[:-4]):
            create_form = True
            break
        create_form = False
    for _, model_config in app_config.get(constants.KEYWORD_PYTHON_MODELS[:-3]).items():
        if model_config.get(constants.KEYWORD_PYTHON_ADMIN[:-3]).get("register"):
            create_admin = True
            break
        create_admin = False

    if constants.create_app:
        _create_app(constants)
    update_settings(constants, config, "INSTALLED_APPS")
    _generate_app_templates_static(app_config.get("webpage"), constants)
    _generate_views(constants)
    _update_main_app_urls(constants)
    _generate_urls(constants)
    _generate_model(app_config.get(constants.KEYWORD_PYTHON_MODELS[:-3]), constants)
    if create_form:
        _generate_form(app_config.get(constants.KEYWORD_PYTHON_MODELS[:-3]), constants)
    if create_admin:
        _generate_admin(app_config.get(constants.KEYWORD_PYTHON_MODELS[:-3]), constants)
