from datetime import datetime
from typing import Optional, Any

from blacksheep.cookies import Cookie
from blacksheep.server.authentication.cookie import CookieAuthentication
from guardpost import Identity, User, Policy
from guardpost.asynchronous.authentication import AuthenticationHandler

from blacksheep import Request, Response

# from db import db_connect
from guardpost.authorization import AuthorizationContext
from guardpost.common import AuthenticatedRequirement
from guardpost.synchronous.authorization import Requirement


class ExampleAuthHandler(CookieAuthentication):
    def __init__(self):
        super(ExampleAuthHandler, self).__init__()

    async def authenticate(self, context: Request) -> Optional[Identity]:
        data = context.cookies
        print(data)
        if data:
            if data['identity'] == 'admin':
                context.identity = Identity({"name": f"{data['identity']}", 'role': 'admin'}, "admin")
                return context.identity
            context.identity = Identity({"name": f"{data['identity']}", 'role': 'user'}, "user")
        else:
            context.identity = None
        return context.identity

    def set_cookies(self, data: Any, response: Response, secure: bool = False) -> None:
        response.set_cookie(
            Cookie(
                'identity',
                data,  # type: ignore
                domain=None,
                path="/",
                http_only=True,
                secure=secure,
                expires=datetime.fromtimestamp(data["exp"]) if "exp" in data else None,
            )
        )

    def handle(self, context: Request):
        identity = context.cookies
        print(identity)
        if identity != {}:
            if identity['identity'] == "admin":
                return True
            else:
                return False
        else:
            return False




def configure_authentication(app):
    app.use_authentication().add(CookieAuthentication())

