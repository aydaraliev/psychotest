from db import db


class VoterModel(db.Model):
    __tablename__ = "voters"

    id = db.Column(db.Integer, primary_key=True)

    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    patronym = db.Column(db.String)
    birthday = db.Column(db.String)
    voting_place = db.Column(db.String)
    parliamentary = db.Column(db.Boolean)
    presidential = db.Column(db.Boolean)

    def __init__(self, firstname, lastname, patronym, birthday, voting_place, parliamentary, presidential):
        self.firstname = firstname
        self.lastname = lastname
        self.patronym = patronym
        self.birthday = birthday
        self.voting_place = voting_place
        self.parliamentary = parliamentary
        self.presidential = presidential

    def json(self):
        return {"firstname": self.firstname, "lastname": self.lastname,
                "patronym": self.patronym, "birthday": self.birthday, "voting_place": self.voting_place,
                "parliamentary": self.parliamentary, "presidential": self.presidential}

    @classmethod
    def find_voter(cls, firstname, lastname, birthday):
        return cls.query.filter_by(firstname=firstname.upper()).filter_by(lastname=lastname.upper()) #.filter_by(birthday=birthday)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()