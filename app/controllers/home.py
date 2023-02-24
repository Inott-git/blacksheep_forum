from typing import Optional, Union
from app.auth import ExampleAuthHandler
from blacksheep.server.authorization import Policy
from blacksheep import redirect, FromCookie, text, Cookie
from blacksheep.server.authentication.cookie import CookieAuthentication
from blacksheep.server.controllers import Controller, get, post
from blacksheep.messages import Response, Request
from guardpost import Identity, User


from db import db_connect
auth = ExampleAuthHandler()

class Home(Controller):

    @get('/')
    async def index(self, request: Request, user: Optional[Identity]):

        await auth.authenticate(request)
        user = None
        data = db_connect.Posts.get_all_posts()
        category = db_connect.Categories.get_all_categories()
        if request.identity:
            user = request.identity.claims
            return self.view('forums', {'user': user['name'], 'data': data, 'category': category})
        else:
            return self.view('forums', {'user': None, 'data': data, 'category': category})



