# Import Flask class from flask package
from flask import Flask

# Create Flask object
app = Flask(__name__)

# Load configurations from config.py
app.config.from_pyfile('config.py', silent=True)

# import Flask routes from view.py
import project.views