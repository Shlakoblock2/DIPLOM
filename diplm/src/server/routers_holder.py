from .router import Router
from .resolver import Resolver
from .routers_resolvers.auth_router import AuthRouter
from .routers_resolvers.deposit_router import TaskRouter
from src.database.models import *

routers = (AuthRouter("Users", Users).router,
           TaskRouter("Deposit", Deposit).router,
           Router("Item", Item).router,
           Router("ItemType", ItemType).router,
           Router("Post", Post).router,
           Router("Personal", Personal).router,
           Router("ClientData", ClientData).router)
