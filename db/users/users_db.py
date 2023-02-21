import bcrypt
from sqlalchemy import select


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

    def check_password(self, login, password):
        stmt = select(self.User).where(self.User.login == login)
        user = self.session.scalar(stmt)
        check = bcrypt.checkpw(password.encode(), user.password)
        if user != None:
            return True
        else:
            return False
