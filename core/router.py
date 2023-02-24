from fastapi import FastAPI

from api import (
	email
)


def init(app: FastAPI):
	app.include_router(
		email.router,
		prefix="",
	)
