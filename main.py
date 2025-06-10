from app.main import app

@app.get("/")
def read_root():
    return {"message": "Hello, World!"} 