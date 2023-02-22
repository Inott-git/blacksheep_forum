from typing import Optional, Union
from app.auth import auth
from blacksheep import redirect, FromCookie, text, Cookie
from blacksheep.server.authentication.cookie import CookieAuthentication
from blacksheep.server.controllers import Controller, get, post
from blacksheep.messages import Response, Request
from guardpost import Identity, User


from db import db_connect


class Home(Controller):

    @get('/')
    async def index(self, request: Request, user: Optional[Identity]):

        await auth.authenticate(request)
        user = request.identity.claims


        data = db_connect.Posts.get_all_posts()
        category = db_connect.Categories.get_all_categories()
        return self.view('forums', {'user':user, 'data': data, 'category': category})

