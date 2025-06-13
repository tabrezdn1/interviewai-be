from fastapi import APIRouter
from app.api.v1.endpoints import analyze, hello

api_router = APIRouter()

api_router.include_router(hello.router, prefix="/hello", tags=["hello"])
api_router.include_router(analyze.router, prefix="/analyze", tags=["analyze"]) 