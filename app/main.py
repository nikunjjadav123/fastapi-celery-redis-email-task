from fastapi import FastAPI
from app.tasks import send_email

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI + Celery + Redis Example"}

@app.post("/send-email/")
def trigger_email(email: str):
    task = send_email.delay(email)  # Send task to Celery via Redis
    return {"task_id": task.id, "status": "Email queued for sending!"}
