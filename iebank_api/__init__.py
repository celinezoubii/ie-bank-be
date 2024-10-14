from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS with specific configuration to allow requests from localhost:8080 (front-end)
CORS(app, resources={r"/*": {"origins": "http://localhost:8081"}})

# Load environment variables from a .env file
load_dotenv()

# Set up the configuration based on the ENV environment variable
if os.getenv('ENV') == 'local':
    print("Running in local mode")
    app.config.from_object('config.LocalConfig')
elif os.getenv('ENV') == 'dev':
    print("Running in development mode")
    app.config.from_object('config.DevelopmentConfig')
elif os.getenv('ENV') == 'ghci':
    print("Running in GitHub CI mode")
    app.config.from_object('config.GithubCIConfig')
else:
    print("Running in production mode")
    app.config.from_object('config.ProductionConfig')

# Initialize SQLAlchemy and CORS
db = SQLAlchemy(app)

# Import routes AFTER initializing db and app to avoid circular imports
from iebank_api import routes
