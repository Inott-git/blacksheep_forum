from blacksheep import Request
from blacksheep.server.controllers import Controller, get, post

from app.controllers.authorization_user import auth
from db import db_connect


class Admin(Controller):
    @get('/admin')
    async def adminchik(self, request: Request):
        check = auth.handle(request)
        category = db_connect.Categories.get_all_categories()
        if check == True:
            return self.view('addpost.html', {'category': category} )
        else:
            return 'You are not admin'

    @post('/admin')
    async def admin(self, request: Request):
        data = await request.form()
        identity = request.cookies
        id_user = db_connect.Users.get_id(identity['identity'])
        cat_id = db_connect.Categories.get_id(data['cat'])
        print(id_user, cat_id)

        db_connect.Posts.add_post(id_user, data['title'], data['description'],cat_id)