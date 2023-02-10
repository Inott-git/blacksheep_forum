from blacksheep import redirect
from blacksheep.server.application import Application
from blacksheep.server.controllers import Controller, get, post
from blacksheep.messages import Response, Request
from db import haching_password
import db
from db import db_connect


class Login(Controller):

    @get('/login')
    async def login_index(self):
        return self.view('index_login')

    @get('/register')
    async def reg_index(self):
        return self.view('index_reg')

    @post('/login')
    async def login(requst: Request):
        data = await requst.form()
        check = db_connect.Users.check_password(data['login'], data['password'])
        if check == True:
            return redirect('/login')
        else:
            return redirect('/')

    @post('/reg')
    async def register(requst: Request):
        data = await requst.form()
        login = data['login']
        print(login)
        password = haching_password.hash_password(data['password'])

        if data['password'] == data['r_password']:
            db_connect.Users.add_user(login, password)
            return redirect('/login')
        else:
            return redirect('/register')




