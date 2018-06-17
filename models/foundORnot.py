from db import db


class FoundOrNotModel(db.Model):

    __tablename__ = "found_not_found"

    id = db.Column(db.Integer, primary_key=True)

    uuid4 = db.Column(db.String)
    found_presidential = db.Column(db.Boolean)
    found_parliamentary = db.Column(db.Boolean)

    def __init__(self, uuid4, found_presidential, found_parliamentary):
        self.uuid4 = uuid4
        self.found_presidential = found_presidential
        self.found_parliamentary = found_parliamentary

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()