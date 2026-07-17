from database.resume_db import save_resume

status = save_resume(
    1,
    "This is my AI generated resume."
)

print(status)