from app import db


class Todo(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    is_completed = db.Column(db.Boolean, nullable=False, default=False)

