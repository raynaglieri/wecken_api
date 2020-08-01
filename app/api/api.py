# Organizes API into submodules.
# Used by FastAPI on instantiation.

from fastapi import APIRouter

from app.api.endpoints import system
from app.api.endpoints import users

api_router = APIRouter()
api_router.include_router(system.router, prefix="/system", tags=["system"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
