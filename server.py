from blacksheep import Application
from db import DataBase

app = Application(show_error_details=True)
db = DataBase('D:\\Проекты\\blacksheep_project\\db\\database.db')


@app.router.get('/user/')
def user(login, password):
    db.Users.add_user(login, password)
    return login, password
