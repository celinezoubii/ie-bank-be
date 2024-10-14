import pytest
from iebank_api import app, db  # Ensure db is imported to manage application context

@pytest.fixture
def testing_client():
    flask_app = app
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory SQLite database for testing
    
    with flask_app.app_context():  # Set up application context for the test
        db.create_all()  # Ensure tables are created
        with flask_app.test_client() as client:
            yield client
        db.drop_all()  # Tear down the database after tests

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/wrong_path')
    assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={
        'name': 'John Doe',
        'currency': '€',
        'country': 'Spain'
    })
    assert response.status_code == 201
