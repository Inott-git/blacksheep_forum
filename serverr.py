from blacksheep import Request, auth, json, ok, Response
from typing import Union, Optional
from guardpost import Identity, Policy, User
from guardpost.asynchronous.authentication import AuthenticationHandler
from guardpost.common import AuthenticatedRequirement
from guardpost.synchronous.authentication import AuthenticationStrategy

from app.program import configure_application


app = configure_application()


