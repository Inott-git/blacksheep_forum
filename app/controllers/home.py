from blacksheep import redirect
from blacksheep.server.controllers import Controller, get, post
from blacksheep.messages import Response, Request
from db import db_connect

class Home(Controller):

    @get('/')
    def index(self):
        data = db_connect.Posts.get_all_posts()
        category = db_connect.Categories.get_all_categories()
        print(data)
        return self.view('forums', {'data': data, 'category':category})