import pytest
from iebank_api import app, db
from iebank_api.models import Account

@pytest.fixture
def new_account():
    """
    Create a new Account instance for testing.
    """
    # Remove 'balance' if it's not a part of the Account model's __init__
    account = Account(name='John Doe', currency='€', country='Spain')
    account.balance = 0.0  # Set balance after creation, if necessary
    return account

@pytest.fixture
def testing_app_context():
    """
    Provide an application context for database-related tests.
    Sets up an in-memory SQLite database for testing.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()  # Create all tables for testing
        yield app
        db.session.remove()
        db.drop_all()  # Tear down the tables after the test

def test_account_add_to_db(testing_app_context, new_account):
    """
    GIVEN a new Account model
    WHEN the Account is added to the database
    THEN check that the account exists in the database
    """
    with testing_app_context.app_context():  # Ensure we are within an app context
        db.session.add(new_account)
        db.session.commit()

        # Retrieve the account from the database
        account_in_db = Account.query.filter_by(account_number=new_account.account_number).first()
        assert account_in_db is not None
        assert account_in_db.name == 'John Doe'
        assert account_in_db.currency == '€'
        assert account_in_db.country == 'Spain'
        assert account_in_db.balance == 0.0  # Check the balance separately
