# main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from apis.general_pages.route_homepage import general_pages_router
from core.config import settings
from db.session import engine
from db.base import Base


def include_router(app):
	app.include_router(general_pages_router)


def create_tables():
	print("create_tables")
	Base.metadata.create_all(bind=engine)


def configure_static(app):
	app.mount('/static', StaticFiles(directory='static'), name='static')


def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	create_tables()
	return app


app = start_application()
