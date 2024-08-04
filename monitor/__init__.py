from flask import Flask

app = Flask(__name__)

from monitor import routes
