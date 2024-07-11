from flask import Blueprint, request, jsonify
from app.services.bill_service import create_bill, get_all_bills, get_bill, update_bill, delete_bill

main = Blueprint('main', __name__)

@main.route('/bills', methods=['POST'])
def add_bill():
    data = request.get_json()
    bill = create_bill(data)
    return jsonify(bill), 201

@main.route('/bills', methods=['GET'])
def get_bills():
    bills = get_all_bills()
    return jsonify(bills)

@main.route('/bills/<int:bill_id>', methods=['GET'])
def get_single_bill(bill_id):
    bill = get_bill(bill_id)
    if bill:
        return jsonify(bill)
    else:
        return jsonify({"message": "Bill not found"}), 404

@main.route('/bills/<int:bill_id>', methods=['PUT'])
def edit_bill(bill_id):
    data = request.get_json()
    bill = update_bill(bill_id, data)
    if bill:
        return jsonify(bill)
    else:
        return jsonify({"message": "Bill not found"}), 404

@main.route('/bills/<int:bill_id>', methods=['DELETE'])
def remove_bill(bill_id):
    bill = delete_bill(bill_id)
    if bill:
        return jsonify({"message": "Bill deleted"})
    else:
        return jsonify({"message": "Bill not found"}), 404
