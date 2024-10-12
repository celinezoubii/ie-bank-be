import pytest
from iebank_api import app

@pytest.fixture
def testing_client():
    flask_app = app
    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as client:
        yield client

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
