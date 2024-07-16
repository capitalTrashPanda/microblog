from flask import Flask

app = Flask(__name__)  # create a flask instance

from app import routes
