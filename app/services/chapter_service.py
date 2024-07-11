from app import db
from app.models import Chapter

def create_chapter(data):
    new_chapter = Chapter(
        title=data['title'],
        content=data['content'],
        section_id=data['section_id'],
        image_url=data.get('image_url')
    )
    db.session.add(new_chapter)
    db.session.commit()
    return new_chapter.to_dict()

def get_all_chapters():
    chapters = Chapter.query.all()
    return [chapter.to_dict() for chapter in chapters]

def get_chapter(chapter_id):
    chapter = Chapter.query.get(chapter_id)
    return chapter.to_dict() if chapter else None

def update_chapter(chapter_id, data):
    chapter = Chapter.query.get(chapter_id)
    if not chapter:
        return None
    chapter.title = data['title']
    chapter.content = data['content']
    chapter.section_id = data['section_id']
    chapter.image_url = data.get('image_url')
    db.session.commit()
    return chapter.to_dict()

def delete_chapter(chapter_id):
    chapter = Chapter.query.get(chapter_id)
    if not chapter:
        return None
    db.session.delete(chapter)
    db.session.commit()
    return chapter.to_dict()
