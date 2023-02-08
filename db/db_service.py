from sqlalchemy import *
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import bcrypt


class Users:

    def __init__(self, session, user, post, category, like, comment):
        self.User = user
        self.Post = post
        self.Category = category
        self.Like = like
        self.Comment = comment

        self.session = session


    def add_user(self, login, password):
        login = login
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        self.session.add(self.User(login=login, password=password))
        self.session.commit()


    def change_user(self, id, login, password):
        stmt = select(self.User).where(self.User.id == id)
        user = self.session.scalar(stmt)
        user.login, user.password = login, password
        self.session.commit()

    def check_password(self, id, password):
        stmt = select(self.User).where(self.User.id == id)
        user = self.session.scalar(stmt)
        bcrypt.checkpw(password.encode(), user.password)


class DataBase:

    def __init__(self, db_path):
        self.engine = create_engine(f'sqlite:///{db_path}')
        self.Base = automap_base()
        self.Base.prepare(autoload_with=self.engine)

        self.User = self.Base.classes.users
        self.Post = self.Base.classes.posts
        self.Category = self.Base.classes.categories
        self.Like = self.Base.classes.likes
        self.Comment = self.Base.classes.comments

        self.session = Session(self.engine)

        self.Users = Users(self.session, self.User, self.Post, self.Category, self.Like, self.Comment)