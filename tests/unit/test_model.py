import pytest
from iebank_api import app, db
from iebank_api.models import Account

@pytest.fixture
def new_account():
    """
    Create a new Account instance for testing.
    """
    account = Account(name='John Doe', currency='€', country='Spain', balance=0.0)
    return account

@pytest.fixture
def testing_app_context():
    """
    Provide an application context for database-related tests.
    """
    with app.app_context():
        db.create_all()  # Create all tables
        yield app
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
