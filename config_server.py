from blacksheep import Application, use_templates
from jinja2 import PackageLoader

from db import DataBase

app = Application(show_error_details=True)
db = DataBase('db/database.db')
view = use_templates(app, loader=PackageLoader('app', 'templates'))
