from datetime import datetime

from jinja2 import Environment, PackageLoader
from roconfiguration import Configuration

from blacksheep.server import Application
from blacksheep.server.templating import use_templates


def configure_templating(application: Application) -> None:
    """
    Configures server side templating engine for HTML views, using Jinja2.
    """
    use_templates(application, PackageLoader("app", "views"))

