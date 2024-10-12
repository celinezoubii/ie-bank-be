import pytest
from iebank_api import app, db
from iebank_api.models import Account


@pytest.fixture(scope='module')
def testing_client():
    flask_app = app
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for tests
    
    # Establish an application context before running the tests.
    with flask_app.app_context():
        db.create_all()  # Create the tables
        yield flask_app.test_client()  # Testing client
        db.drop_all()  # Cleanup after tests

