from sqlalchemy import select
import datetime


class Posts:
    def __init__(self, session, user, post, category, like, comment):
        self.User = user
        self.Post = post
        self.Category = category
        self.Like = like
        self.Comment = comment

        self.session = session

    def get_all_posts(self):
        stmt = select(self.Post.title, self.Post.description, self.Post.time_post, self.User.login, self.Category.title).join_from(self.Post, self.User).join_from(self.Post, self.Category)
        data = self.session.execute(stmt).all()
        return data

    def add_post(self, user_id, title, description, categories_id):
        self.session.add(self.Post(user_id=user_id, title=title, description=description, time_post=datetime.datetime.now(), categories_id=categories_id))
        self.session.commit()

    def change_post(self, id, title, description, categories_id):
        post = self.session.get(self.Post, id)
        post.title, post.description, post.categories_id = title, description, categories_id
        self.session.commit()

    def delete_post(self, id):
        post = self.session.get(self.Post, id)
        self.session.delete(post)
        self.session.commit()


class Categories:

    def __init__(self, session, category):
        self.Category = category

        self.session = session

    def get_category_by_id(self, id):
        return self.session.scalar(select(self.Category).where(self.Category.id==id))

    def get_all_categories(self):
        data = self.session.execute(select(self.Category.title)).all()
        return data

    def add_category(self, title):
        self.session.add(self.Category(title=title))
        self.session.commit()
