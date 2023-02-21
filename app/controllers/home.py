from typing import Optional, Union

from blacksheep import redirect, FromCookie, text, Cookie
from blacksheep.server.controllers import Controller, get, post
from blacksheep.messages import Response, Request
from guardpost import Identity, User


from db import db_connect


class Home(Controller):

    @get('/')
    async def index(self, request: Request, user: Optional[Identity]):
        user = request.cookies

        data = db_connect.Posts.get_all_posts()
        category = db_connect.Categories.get_all_categories()
        return self.view('forums', {'user': list(user)[0], 'data': data, 'category': category})

