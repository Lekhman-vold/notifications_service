import logging
from fastapi import FastAPI

from core import router
from core.settings import get_settings

settings = get_settings()


def get_logger(name):
	logger = logging.getLogger(name)
	return logger


def create_api_app(dependency_overrides=None, logger=get_logger("api")):
	app = FastAPI(logging=logger)

	if dependency_overrides:
		app.dependency_overrides.update(dependency_overrides)

	router.init(app)

	logger.info("started api service")
	return app


app = create_api_app()
