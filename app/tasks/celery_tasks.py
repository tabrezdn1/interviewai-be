from celery import Celery
import time
import logging
from app.core.config import get_settings
from app.services.analysis import simulate_llm_analysis

settings = get_settings()

# Initialize Celery with Redis as both broker and backend
celery = Celery(
    'tasks',
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

# Configure logging
logging.basicConfig(level=getattr(logging, settings.LOG_LEVEL))
logger = logging.getLogger(__name__)

@celery.task
def analyze_basic(transcript):
    logger.info("Starting basic analysis...")
    # Simulate basic analysis using LLM
    time.sleep(5)  # Simulate processing time
    logger.info("Basic analysis completed!")
    return simulate_llm_analysis(transcript, "basic")

@celery.task
def analyze_pro(transcript):
    logger.info("Starting pro analysis...")
    # Simulate pro analysis using LLM
    time.sleep(10)  # Simulate processing time
    logger.info("Pro analysis completed!")
    return simulate_llm_analysis(transcript, "pro")

@celery.task
def analyze_advanced(transcript):
    logger.info("Starting advanced analysis...")
    # Simulate advanced analysis using LLM
    time.sleep(15)  # Simulate processing time
    logger.info("Advanced analysis completed!")
    return simulate_llm_analysis(transcript, "advanced") 