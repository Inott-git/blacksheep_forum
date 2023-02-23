from typing import Optional
from app.auth import ExampleAuthHandler
from blacksheep.server.authentication.cookie import CookieAuthentication
from blacksheep.server.authentication.oidc import CookiesTokensStore
from guardpost.common import AuthenticatedRequirement

from blacksheep import redirect, json
from blacksheep.server.controllers import Controller, get, post
from blacksheep.messages import Request, Response
from guardpost import Identity, Policy, authorization

from db import haching_password

from db import db_connect


class Login(Controller):

    @get('/login')
    async def login_index(self, request: Request):

        return self.view('index_login')

    @get('/register')
    async def reg_index(self):
        return self.view('index_reg')

    @post('/sing')
    async def login(self, requstt: Request) -> Response:
        data = await requstt.form()

        check = db_connect.Users.check_password(data['login'], data['password'])

        if check:
            response = self.redirect('/')
            # auth = CookiesTokensStore()
            authhh = ExampleAuthHandler()
            authhh.set_cookies(f'{data["login"]}', response,  secure=True)

        else:
            response = self.redirect('/login')
        return response

    @post('/log_out')
    async def logout(self, request: Request) -> Response:
        authh = ExampleAuthHandler()
        respounce = self.redirect('/')
        authh.unset_cookie(respounce)
        return respounce

    @post('/reg')
    async def register(requst: Request):
        data = await requst.form()
        login = data['login']

        password = haching_password.hash_password(data['password'])

        if data['password'] == data['r_password']:
            db_connect.Users.add_user(login, password)
            return redirect('/login')
        else:
            return redirect('/register')




