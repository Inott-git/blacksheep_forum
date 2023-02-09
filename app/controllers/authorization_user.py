from blacksheep.server.controllers import Controller, get
from config_server import app, view, db
from blacksheep import Response, Request, FromJSON, FromForm, redirect


class Login(Controller):

    @app.router.get('/')
    async def login_index(self):
        return view('login', {})

    @app.router.post('/login')
    async def login(requst: Request):
        data = await requst.form()

        check = db.Users.check_password(data['login'], data['password'])
        if check == True:
            return redirect('/login')
        else:
            return redirect('/')



