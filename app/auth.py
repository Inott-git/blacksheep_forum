from typing import Optional

from blacksheep.server.authentication.cookie import CookieAuthentication
from guardpost import Identity, User, Policy
from guardpost.asynchronous.authentication import AuthenticationHandler

from blacksheep import Request

# from db import db_connect
from guardpost.common import AuthenticatedRequirement

auth = CookieAuthentication()
class ExampleAuthHandler(AuthenticationHandler):
    def __init__(self):
        pass

    async def authenticate(self, context: Request) -> Optional[Identity]:
        header_value = context.get_first_header(b"Authorization")
        header_value = True
        if header_value:

            context.identity = Identity({"name": "Jan Kowalski"}, "MOCK")
        else:
            context.identity = None
        return context.identity


def configure_authentication(app):
    app.use_authentication().add(ExampleAuthHandler())
