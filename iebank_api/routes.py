from flask import jsonify, request
from iebank_api import app, db
from iebank_api.models import Account

# Route to create a new bank account
@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.get_json()
    name = data.get('name')
    balance = data.get('balance', 0.0)
    currency = data.get('currency', "€")
    country = data.get('country')

    if not name or not currency or not country:
        return jsonify({'error': 'Missing required fields'}), 400

    new_account = Account(name=name, currency=currency, country=country)
    new_account.balance = balance

    db.session.add(new_account)
    db.session.commit()

    return jsonify({
        'message': 'Account created successfully!',
        'account': {
            'name': new_account.name,
            'account_number': new_account.account_number,
            'balance': new_account.balance,
            'currency': new_account.currency,
            'status': new_account.status,
            'country': new_account.country
        }
    }), 201

# Route to retrieve an account by its ID
@app.route('/accounts/<int:id>', methods=['GET'])
def get_account(id):
    account = Account.query.get(id)
    if not account:
        return jsonify({'error': 'Account not found'}), 404

    return jsonify({
        'id': account.id,
        'name': account.name,
        'account_number': account.account_number,
        'balance': account.balance,
        'currency': account.currency,
        'status': account.status,
        'country': account.country
    })

# Route to update an account's details
@app.route('/accounts/<int:id>', methods=['PUT'])
def update_account(id):
    account = Account.query.get(id)

    if not account:
        return jsonify({'error': 'Account not found'}), 404

    data = request.get_json()
    account.name = data.get('name', account.name)
    account.balance = data.get('balance', account.balance)
    account.currency = data.get('currency', account.currency)
    account.country = data.get('country', account.country)

    db.session.commit()

    return jsonify({
        'message': 'Account updated successfully!',
        'account': {
            'id': account.id,
            'name': account.name,
            'account_number': account.account_number,
            'balance': account.balance,
            'currency': account.currency,
            'status': account.status,
            'country': account.country
        }
    })

# Route to delete an account by its ID
@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    account = Account.query.get(id)

    if not account:
        return jsonify({'error': 'Account not found'}), 404

    db.session.delete(account)
    db.session.commit()

    return jsonify({'message': 'Account deleted successfully!'})
@app.route('/')
def home():
    return "Welcome to the IE Bank API!"

