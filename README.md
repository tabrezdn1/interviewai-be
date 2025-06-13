# Interview AI Backend

A FastAPI-based backend service for analyzing interview transcripts using LLM. The service provides different levels of analysis (basic, pro, and advanced) and processes them asynchronously using Celery.

## Project Structure

```
interviewai-be/
├── app/
│   ├── api/                    # API endpoints
│   │   ├── v1/                # API version 1
│   │   │   ├── endpoints/     # Individual endpoint modules
│   │   │   │   ├── analyze.py # Analysis endpoints
│   │   │   │   └── hello.py   # Hello world endpoint
│   │   │   └── router.py      # API router configuration
│   │   ├── core/                   # Core functionality
│   │   │   └── config.py          # Application settings
│   │   ├── services/              # Business logic
│   │   │   └── analysis.py        # Analysis service
│   │   └── tasks/                 # Celery tasks
│   │       └── celery_tasks.py    # Task definitions
│   ├── tests/                     # Test files
│   ├── .env                       # Environment variables
│   ├── docker-compose.yml         # Docker services configuration
│   ├── Dockerfile                 # Docker image configuration
│   └── requirements.txt           # Python dependencies
```

## Features

- Asynchronous processing of interview analysis
- Multiple analysis levels (basic, pro, advanced)
- Task status tracking
- Dockerized deployment
- Redis for task queue and results backend
- Celery for task management

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd interviewai-be
```

2. Create a `.env` file with the following variables:
```env
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=True
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=0
LOG_LEVEL=INFO
```

3. Run with Docker Compose:
```bash
docker compose up --build
```

## API Endpoints

### Hello World
- `GET /api/v1/hello`
- Returns a welcome page

### Analysis
- `POST /api/v1/analyze`
  - Request body:
    ```json
    {
      "transcript": "Interview transcript text...",
      "userId": "user123",
      "requestedReports": ["basic", "pro", "advanced"],
      "metadata": {
        "interviewId": "interview456",
        "timestamp": "2023-10-01T12:00:00Z"
      }
    }
    ```
  - Returns task IDs for tracking

- `GET /api/v1/analyze/status/{taskId}`
  - Returns task status and result if completed

## Adding New Features

### 1. Adding a New Endpoint

1. Create a new file in `app/api/v1/endpoints/`:
```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def new_endpoint():
    return {"message": "New endpoint"}
```

2. Add the router to `app/api/v1/router.py`:
```python
from app.api.v1.endpoints import new_endpoint

api_router.include_router(new_endpoint.router, prefix="/new", tags=["new"])
```

### 2. Adding a New Service

1. Create a new file in `app/services/`:
```python
def new_service():
    # Business logic here
    return result
```

2. Import and use in your endpoints or tasks:
```python
from app.services.new_service import new_service
```

### 3. Adding a New Celery Task

1. Add the task to `app/tasks/celery_tasks.py`:
```python
@celery.task
def new_task():
    # Task logic here
    return result
```

2. Import and use in your endpoints:
```python
from app.tasks.celery_tasks import new_task
```

## Development

### Running Tests
```bash
# Add test commands here when tests are implemented
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Document functions and classes

### Adding Dependencies
1. Add to `requirements.txt`
2. Rebuild Docker containers:
```bash
docker compose up --build
```

## Deployment

### Production Considerations
1. Set `DEBUG=False` in `.env`
2. Configure proper CORS settings
3. Set up proper logging
4. Configure proper security measures

### Scaling
- The application is designed to scale horizontally
- Celery workers can be scaled independently
- Redis can be configured for high availability

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
