from app.models import db, Bill, Part, Section, Chapter

def create_bill(data):
    bill = Bill(
        title=data['title'],
        year=data['year'],
        clauses=data['clauses'],
        category=data['category']
    )
    db.session.add(bill)
    db.session.commit()
    return bill.to_dict()

def get_all_bills():
    return [bill.to_dict() for bill in Bill.query.all()]

def get_bill(bill_id):
    bill = Bill.query.get(bill_id)
    return bill.to_dict() if bill else None

def update_bill(bill_id, data):
    bill = Bill.query.get(bill_id)
    if bill:
        bill.title = data['title']
        bill.year = data['year']
        bill.clauses = data['clauses']
        bill.category = data['category']
        db.session.commit()
        return bill.to_dict()
    return None

def delete_bill(bill_id):
    bill = Bill.query.get(bill_id)
    if bill:
        db.session.delete(bill)
        db.session.commit()
        return bill.to_dict()
    return None
