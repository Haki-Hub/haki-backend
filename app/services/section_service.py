from app import db
from app.models import Section

def create_section(data):
    new_section = Section(
        title=data['title'],
        part_id=data['part_id']
    )
    db.session.add(new_section)
    db.session.commit()
    return new_section.to_dict()

def get_all_sections():
    sections = Section.query.all()
    return [section.to_dict() for section in sections]

def get_section(section_id):
    section = Section.query.get(section_id)
    return section.to_dict() if section else None

def update_section(section_id, data):
    section = Section.query.get(section_id)
    if not section:
        return None
    section.title = data['title']
    section.part_id = data['part_id']
    db.session.commit()
    return section.to_dict()

def delete_section(section_id):
    section = Section.query.get(section_id)
    if not section:
        return None
    db.session.delete(section)
    db.session.commit()
    return section.to_dict()
