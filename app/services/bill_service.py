from app import db
from app.models import Category, Bill, Part, Section, Chapter

def create_full_bill(data):
    try:
        # Ensure required fields are present
        required_fields = ['title', 'year', 'clauses', 'category', 'parts']
        for field in required_fields:
            if field not in data:
                return {"message": f"'{field}' is required"}, 400

        # Create Category if provided
        category_name = data.get('category')
        category = Category.query.filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            db.session.add(category)
            db.session.flush()  # Ensures the category_id is generated

        # Create Bill
        new_bill = Bill(
            title=data['title'],
            year=data['year'],
            clauses=data['clauses'],
            category_id=category.category_id
        )
        db.session.add(new_bill)
        db.session.flush()  # Ensures the bill_id is generated

        # Create Parts
        parts_data = data.get('parts', [])
        for part_data in parts_data:
            new_part = Part(
                title=part_data['title'],
                bill_id=new_bill.bill_id
            )
            db.session.add(new_part)
            db.session.flush()  # Ensures the part_id is generated

            # Create Sections
            sections_data = part_data.get('sections', [])
            for section_data in sections_data:
                new_section = Section(
                    title=section_data['title'],
                    part_id=new_part.part_id
                )
                db.session.add(new_section)
                db.session.flush()  # Ensures the section_id is generated

                # Create Chapters
                chapters_data = section_data.get('chapters', [])
                for chapter_data in chapters_data:
                    new_chapter = Chapter(
                        title=chapter_data['title'],
                        content=chapter_data['content'],
                        section_id=new_section.section_id,
                        image_url=chapter_data.get('image_url')
                    )
                    db.session.add(new_chapter)

        db.session.commit()
        return new_bill.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return {"message": str(e)}, 500

def get_all_bills():
    bills = Bill.query.all()
    return [bill.to_dict() for bill in bills]

def get_bill(bill_id):
    bill = Bill.query.get(bill_id)
    return bill.to_dict() if bill else None

def update_bill(bill_id, data):
    bill = Bill.query.get(bill_id)
    if not bill:
        return None
    bill.title = data['title']
    bill.year = data['year']
    bill.clauses = data['clauses']
    bill.category_id = data['category_id']
    db.session.commit()
    return bill.to_dict()

def delete_bill(bill_id):
    bill = Bill.query.get(bill_id)
    if not bill:
        return None
    db.session.delete(bill)
    db.session.commit()
    return bill.to_dict()
