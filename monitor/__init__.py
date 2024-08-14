from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '24104e2afa361af07d76fa500f6b8fd42f007b944e489abf'
from monitor import routes
