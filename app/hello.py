from fastapi import APIRouter, Response

router = APIRouter()

@router.get("/hello")
def hello():
    html_content = """
    <html>
        <head><title>Hello</title></head>
        <body style='text-align:center;'>
            <h1>Hey this is backend for Interview AI!</h1>
            <img src='https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif' alt='Hello GIF' />
        </body>
    </html>
    """
    return Response(content=html_content, media_type="text/html") 