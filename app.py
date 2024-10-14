from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from iebank_api import routes, models

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use your actual DB URL here

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)

from iebank_api import app

if __name__ == '__main__':
    app.run(debug=True)

