from email_validator import validate_email
from pydantic import BaseModel, EmailStr, validator


class SendEmailModel(BaseModel):
	subject: str
	from_email: str
	to_email: EmailStr
	html: str

	@validator('to_email')
	def validate_email(cls, value):
		if not validate_email(value):
			raise ValueError('email is not valid')
		return value
