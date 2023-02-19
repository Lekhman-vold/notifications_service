from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import validator

from starlette import status
from validate_email import validate_email

app = FastAPI()


class EmailModel(BaseModel):
    message_type: str
    from_email: str
    to_email: str

    @validator('from_email', 'to_email')
    def validate_email(cls, value):
        if not validate_email(value):
            raise ValueError('email is not valid')
        return value


@app.post("/send-email/", status_code=status.HTTP_200_OK)
async def sender(schema: EmailModel):
    schema = schema.dict()
    # TODO: implement email sending logic
    return schema
