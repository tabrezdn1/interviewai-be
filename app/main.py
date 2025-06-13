from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.api.v1.router import api_router
# from app.mcp import router as mcp_router
# from app.a2a import router as a2a_router

settings = get_settings()

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    debug=settings.DEBUG
)

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.ALLOWED_METHODS,
    allow_headers=settings.ALLOWED_HEADERS,
)

# Include API router
app.include_router(api_router, prefix=settings.API_PREFIX)
# app.include_router(mcp_router)
# app.include_router(a2a_router)

# To add more endpoints, create a new file (e.g., app/foo.py) with a router and include it here:
# from app.foo import router as foo_router
# app.include_router(foo_router) 