from app import db
from app.models import Part

def create_part(data):
    new_part = Part(
        title=data['title'],
        bill_id=data['bill_id']
    )
    db.session.add(new_part)
    db.session.commit()
    return new_part.to_dict()

def get_all_parts():
    parts = Part.query.all()
    return [part.to_dict() for part in parts]

def get_part(part_id):
    part = Part.query.get(part_id)
    return part.to_dict() if part else None

def update_part(part_id, data):
    part = Part.query.get(part_id)
    if not part:
        return None
    part.title = data['title']
    part.bill_id = data['bill_id']
    db.session.commit()
    return part.to_dict()

def delete_part(part_id):
    part = Part.query.get(part_id)
    if not part:
        return None
    db.session.delete(part)
    db.session.commit()
    return part.to_dict()
