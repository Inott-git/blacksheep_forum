from sqlalchemy import *
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from db.users import Users
from db.posts import Posts, Categories


class DataBase:

    def __init__(self, db_path):
        self._engine = create_engine(f'sqlite:///{db_path}')
        self._Base = automap_base()
        self._Base.prepare(autoload_with=self._engine)

        self._User = self._Base.classes.users
        self._Post = self._Base.classes.posts
        self._Category = self._Base.classes.categories
        self._Like = self._Base.classes.likes
        self._Comment = self._Base.classes.comments

        self._session = Session(self._engine)

        self.Users = Users(self._session, self._User, self._Post, self._Category, self._Like, self._Comment)
        self.Posts = Posts(self._session, self._User, self._Post, self._Category, self._Like, self._Comment)
        self.Categories = Categories(self._session, self._Category)

db_connect = DataBase('db/database.db')
