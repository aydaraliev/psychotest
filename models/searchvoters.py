from db import db


class SearchVoterModel(db.Model):
    __tablename__ = "searchvoters"

    id = db.Column(db.Integer, primary_key=True)

    uuid4 = db.Column(db.String)
    birthday = db.Column(db.String)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)

    def __init__(self, uuid4, birthday, firstname, lastname):
        self.uuid4 = uuid4
        self.birthday = birthday
        self.firstname = firstname
        self.lastname = lastname

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



