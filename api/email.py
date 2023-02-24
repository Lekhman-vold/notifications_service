from datetime import datetime

from fastapi import HTTPException, APIRouter
from starlette import status
from email.mime.text import MIMEText
from smtplib import SMTP_SSL

from core.settings import get_settings
from schemas.email import SendEmailModel

settings = get_settings()

router = APIRouter()


@router.post("/send-email/", status_code=status.HTTP_200_OK)
async def sender(schema: SendEmailModel):
	subject = schema.subject
	from_email = schema.from_email
	to_email = schema.to_email
	html = schema.html

	try:
		msg = MIMEText(html, "html")
		msg['Subject'] = subject
		msg['From'] = from_email
		msg['To'] = to_email

		# Connect to the email server
		server = SMTP_SSL(
			settings.smtp.server,
			settings.smtp.port
		)
		server.login(
			settings.smtp.username,
			settings.smtp.password
		)

		# Send the email
		server.send_message(msg)
		server.quit()
		return {
			"message": "email sent successfully {0}".format(datetime.now())
		}

	except Exception as e:
		raise HTTPException(status_code=500, detail=e)
