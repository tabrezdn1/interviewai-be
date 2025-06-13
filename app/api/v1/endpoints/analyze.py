from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from app.tasks.celery_tasks import analyze_basic, analyze_pro, analyze_advanced
from celery.result import AsyncResult
import datetime

router = APIRouter()

class AnalyzeRequest(BaseModel):
    transcript: str = Field(..., example="Interviewer: Tell me about yourself. Candidate: I have 5 years of experience...")
    userId: str = Field(..., example="user123")
    requestedReports: List[str] = Field(..., example=["basic", "pro", "advanced"])
    metadata: Optional[dict] = Field(None, example={"interviewId": "interview456", "timestamp": "2023-10-01T12:00:00Z"})

@router.post("/")
async def analyze(request: AnalyzeRequest):
    task_ids: Dict[str, str] = {}

    # Trigger Celery tasks based on requested reports
    if "basic" in request.requestedReports:
        task = analyze_basic.delay(request.transcript)
        task_ids["basic"] = task.id
    if "pro" in request.requestedReports:
        task = analyze_pro.delay(request.transcript)
        task_ids["pro"] = task.id
    if "advanced" in request.requestedReports:
        task = analyze_advanced.delay(request.transcript)
        task_ids["advanced"] = task.id

    return {
        "message": "Report submitted successfully",
        "taskIds": task_ids
    }

@router.get("/status/{taskId}")
async def get_status(taskId: str):
    # Get the Celery task result
    task_result = AsyncResult(taskId)
    
    if task_result.ready():
        # Task is complete, return the result
        return {"status": "completed", "result": task_result.result}
    else:
        # Task is still in progress
        return {
            "status": "in_progress",
            "state": task_result.state
        } 