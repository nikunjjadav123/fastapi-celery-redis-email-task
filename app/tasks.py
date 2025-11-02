from app.celery_app import celery_app

@celery_app.task(name="app.tasks.send_email")
def send_email(recipient):
    print(f"📧 Sending email to {recipient}")
    return f"Email sent to {recipient}"
