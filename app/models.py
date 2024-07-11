from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Bill(db.Model):
    __tablename__ = 'bills'
    bill_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    clauses = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(255), nullable=False)
    parts = db.relationship('Part', backref='bill', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'bill_id': self.bill_id,
            'title': self.title,
            'year': self.year,
            'clauses': self.clauses,
            'category': self.category,
            'parts': [part.to_dict() for part in self.parts]
        }

class Part(db.Model):
    __tablename__ = 'parts'
    part_id = db.Column(db.Integer, primary_key=True)
    bill_id = db.Column(db.Integer, db.ForeignKey('bills.bill_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    sections = db.relationship('Section', backref='part', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'part_id': self.part_id,
            'bill_id': self.bill_id,
            'title': self.title,
            'sections': [section.to_dict() for section in self.sections]
        }

class Section(db.Model):
    __tablename__ = 'sections'
    section_id = db.Column(db.Integer, primary_key=True)
    part_id = db.Column(db.Integer, db.ForeignKey('parts.part_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    chapters = db.relationship('Chapter', backref='section', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'section_id': self.section_id,
            'part_id': self.part_id,
            'title': self.title,
            'chapters': [chapter.to_dict() for chapter in self.chapters]
        }

class Chapter(db.Model):
    __tablename__ = 'chapters'
    chapter_id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, db.ForeignKey('sections.section_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            'chapter_id': self.chapter_id,
            'section_id': self.section_id,
            'title': self.title,
            'content': self.content,
            'image_url': self.image_url
        }
