# FastAPI Hello World App

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the app

```bash
uvicorn main:app --reload
```

## Run with Docker

Build the Docker image:

```bash
docker build -t fastapi-hello .
```

Run the container:

```bash
docker run -p 8000:8000 fastapi-hello
```

## Run with Docker Compose

Start the app using Docker Compose:

```bash
docker compose up --build
```

## CORS and Proxy Settings

- CORS (Cross-Origin Resource Sharing) is enabled for all origins in development, so you can access the API from any frontend or proxy without issues.
- For production, restrict `allow_origins` in `app/main.py` to trusted domains for better security.

Visit [http://localhost:8000](http://localhost:8000) to see the Hello World endpoint. 