from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    extraversion = db.Column(db.Integer)
    neuroticism  = db.Column(db.Integer)
    openness = db.Column(db.Integer)
    consciousness = db.Column(db.Integer)
    friendly = db.Column(db.Integer)

    def __init__(self, extraversion, neuroticism, openness, consciousness, friendly):
        self.extraversion = extraversion
        self.neuroticism = neuroticism
        self.openness = openness
        self.consciousness = consciousness
        self.friendly = friendly

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()