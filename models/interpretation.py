'''from db import db

class InterpretationModel(db.Model):

    __tablename__ = 'interpretation'

    id = db.Column(db.Integer, primary_key=True)

    extraversion = db.Column(db.Text)
    neuroticism = db.Column(db.Text)
    openness = db.Column(db.Text)
    consciousness = db.Column(db.Text)
    friendly = db.Column(db.Text)

    def __init__(self):'''