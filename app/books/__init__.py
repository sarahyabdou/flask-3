
from flask import Blueprint

book_blueprint = Blueprint("books",__name__,url_prefix="/" )

from app.books import views
from app.books import api_views