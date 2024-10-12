import pytest
from iebank_api import db
from iebank_api.models import Account

@pytest.fixture(scope='module')
def new_account():
    account = Account(name='Test Account', currency='€', country='Spain')
    return account

def test_new_account(new_account):
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check if the name, currency, and country fields are defined correctly
    """
    assert new_account.name == 'Test Account'
    assert new_account.currency == '€'
    assert new_account.country == 'Spain'

def test_account_add_to_db(new_account):
    """
    GIVEN a new Account model
    WHEN the Account is added to the database
    THEN check that the account exists in the database
    """
    db.session.add(new_account)
    db.session.commit()
    assert new_account in db.session
