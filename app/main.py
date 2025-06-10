from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.hello import router as hello_router
# from app.mcp import router as mcp_router
# from app.a2a import router as a2a_router

app = FastAPI()

# CORS settings: allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers for modular endpoints
app.include_router(hello_router)
# app.include_router(mcp_router)
# app.include_router(a2a_router)

# To add more endpoints, create a new file (e.g., app/foo.py) with a router and include it here:
# from app.foo import router as foo_router
# app.include_router(foo_router) 