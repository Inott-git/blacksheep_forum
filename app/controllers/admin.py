from blacksheep import Request
from blacksheep.server.controllers import Controller, get, post

from app.controllers.authorization_user import auth
from db import db_connect


class Admin(Controller):
    @get('/add_post')
    async def addpost(self, request: Request):
        category = db_connect.Categories.get_all_categories()
        category = list(map(list, category))
        return self.view('addpost.html', {'category': category} )

    @post('/add_post')
    async def add_post(self, request: Request):
        data = await request.form()
        identity = request.cookies
        id_user = db_connect.Users.get_id(identity['identity'])
        cat_id = db_connect.Categories.get_id(data['cat'])
        db_connect.Posts.add_post(user_id=id_user, title=data['title'], description=data['description'], cat_id=cat_id)
        respounse = self.redirect('/')
        return respounse

    @get('/add_cat')
    async def addcat(self, request: Request):
        check = auth.handle(request)
        if check:
            return self.view('addcat.html')
        else:
            return 'You are not admin'

    @post('/add_cat')
    async def add_cat(self, request: Request):
        data = await request.form()
        db_connect.Categories.add_category(data['title'])
        return self.redirect('/')