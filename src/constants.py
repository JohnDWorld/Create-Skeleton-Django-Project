import sys

from pathlib import Path
from utils import slugify


class Constants:
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Keys Words
    KEYWORD_JSON_NAME = "project_config.json"
    KEYWORD_TEMPLATES = "templates"
    KEYWORD_STATIC = "static"
    KEYWORD_HTML_BASE = "base.html"
    KEYWORD_HTML_ERROR = "404.html"
    KEYWORD_HTML_HOMEPAGE = "homepage.html"
    KEYWORD_CSS_APP = "app.css"
    KEYWORD_CSS_STYLE = "style.css"
    KEYWORD_PYTHON_URLS = "urls.py"
    KEYWORD_PYTHON_URLS_MAIN = "urls_main.py"
    KEYWORD_PYTHON_SETTINGS = "settings.py"
    KEYWORD_PYTHON_ADMIN = "admin.py"
    KEYWORD_PYTHON_MODELS = "models.py"
    KEYWORD_PYTHON_VIEWS = "views.py"
    KEYWORD_PYTHON_FORMS = "forms.py"

    # Pattern HTML Files to find
    PATTERN_LANGUAGE_HTML = "{language_html}"
    PATTERN_BOOTSTRAP_LINK = "{bootstrap_css}"
    PATTERN_BOOTSTRAP_SCRIPT = "{bootstrap_script}"
    PATTERN_APP_NAME = "{app_name}"

    # Django Fields
    CHARFIELD = {"CharField": "max_length=200"}
    EMAILFIELD = "EmailField"
    INTEGERFIELD = "IntegerField"
    DATEFIELD = "DateField"
    DATETIMEFIELD = {"DateTimeField": "auto_now_add=True"}
    SLUGFIELD = {"SlugField": "unique=True"}
    BOOLEANFIELD = "BooleanField"
    FLOATFIELD = "FloatField"
    FILEFIELD = "FileField"
    IMAGEFIELD = {"ImageField": 'upload_to="", null=True'}
    TEXTFIELD = {"TextField": "max_length=500"}
    URLFIELD = "URLField"
    FOREIGNKEY = "ForeignKey"
    MANYTOMANYFIELD = "ManyToManyField"
    ONETOONEFIELD = "OneToOneField"

    # Directories to find files in the project
    SRC_DIR = BASE_DIR / "src"
    TEMPLATES_DIR = BASE_DIR / KEYWORD_TEMPLATES
    PROJECTS_DIR = BASE_DIR / "projects"
    HTML_DIR = TEMPLATES_DIR / "html"
    PYTHON_DIR = TEMPLATES_DIR / "python"

    # Files to find
    FILE_JSON_NAME = SRC_DIR / KEYWORD_JSON_NAME
    FILE_HTML_BASE = HTML_DIR / KEYWORD_HTML_BASE
    FILE_HTML_ERROR = HTML_DIR / KEYWORD_HTML_ERROR
    FILE_HTML_HOMEPAGE = HTML_DIR / KEYWORD_HTML_HOMEPAGE
    FILE_PYTHON_VIEWS = PYTHON_DIR / KEYWORD_PYTHON_VIEWS
    FILE_PYTHON_URLS = PYTHON_DIR / KEYWORD_PYTHON_URLS

    # Define the paths to the Python and pip executables
    PATH_PYTHON = (
        SRC_DIR / "venv" / "Scripts" / "python.exe"
        if sys.platform == "win32"
        else SRC_DIR / "venv" / "bin" / "python"
    )

    # Define Bootstrap link and scripts
    BALISE_BOOTSTRAP_LINK = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">'
    BALISE_BOOTSTRAP_SCRIPT = f'<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>\n  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>'

    # Define the time to wait after each action
    SLEEP_TIME = 1

    # The middleware line to change language of the project
    MIDDLEWARE = "django.middleware.locale.LocaleMiddleware"

    def add_project(self, config: str) -> None:
        """Define the constants project."""
        self.__setattr__(
            "create_project",
            True,
        )
        self.__setattr__(
            "PRJ_DIR",
            Constants.PROJECTS_DIR / config["project"],
        )
        self.__setattr__(
            "PRJ_DIR_TEMPLATES",
            self.PRJ_DIR / self.KEYWORD_TEMPLATES,
        )
        self.__setattr__(
            "PRJ_DIR_STATIC",
            self.PRJ_DIR / self.KEYWORD_STATIC,
        )
        self.__setattr__(
            "MAIN_APP_FILE_HTML_BASE",
            self.PRJ_DIR_TEMPLATES / self.KEYWORD_HTML_BASE,
        )
        self.__setattr__(
            "MAIN_APP_FILE_HTML_ERROR",
            self.PRJ_DIR_TEMPLATES / self.KEYWORD_HTML_ERROR,
        )
        self.__setattr__(
            "MAIN_APP_FILE_CSS_APP",
            self.PRJ_DIR_STATIC / self.KEYWORD_CSS_APP,
        )
        self.__setattr__(
            "MAIN_APP_FILE_URLS",
            self.PRJ_DIR / config["slug"] / self.KEYWORD_PYTHON_URLS,
        )
        self.__setattr__(
            "MAIN_APP_FILE_URLS_MAIN",
            self.PYTHON_DIR / self.KEYWORD_PYTHON_URLS_MAIN,
        )
        self.__setattr__(
            "MAIN_APP_FILE_SETTINGS",
            self.PRJ_DIR / config["slug"] / self.KEYWORD_PYTHON_SETTINGS,
        )

    def add_app(self, app_name: str) -> None:
        """Define the constants app."""
        slug_app_name = slugify(self.PATH_PYTHON, app_name)
        self.__setattr__(
            "create_app",
            True,
        )
        self.__setattr__(
            "SLUG_APP_NAME",
            slug_app_name,
        )
        self.__setattr__("APP_DIR", self.PRJ_DIR / self.SLUG_APP_NAME)
        self.__setattr__(
            "APP_DIR_TEMPLATES",
            self.PRJ_DIR
            / self.SLUG_APP_NAME
            / self.KEYWORD_TEMPLATES
            / self.SLUG_APP_NAME,
        )
        self.__setattr__(
            "APP_DIR_STATIC",
            self.PRJ_DIR
            / self.SLUG_APP_NAME
            / self.KEYWORD_STATIC
            / self.SLUG_APP_NAME,
        )
        self.__setattr__(
            "APP_FILE_ADMIN",
            self.PRJ_DIR / self.SLUG_APP_NAME / self.KEYWORD_PYTHON_ADMIN,
        )
        self.__setattr__(
            "APP_FILE_MODELS",
            self.PRJ_DIR / self.SLUG_APP_NAME / self.KEYWORD_PYTHON_MODELS,
        )
        self.__setattr__(
            "APP_FILE_VIEWS",
            self.PRJ_DIR / self.SLUG_APP_NAME / self.KEYWORD_PYTHON_VIEWS,
        )
        self.__setattr__(
            "APP_FILE_FORMS",
            self.PRJ_DIR / self.SLUG_APP_NAME / self.KEYWORD_PYTHON_FORMS,
        )
        self.__setattr__(
            "APP_FILE_URLS",
            self.PRJ_DIR / self.SLUG_APP_NAME / self.KEYWORD_PYTHON_URLS,
        )
