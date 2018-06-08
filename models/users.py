from db import db


class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    extraversion = db.Column(db.Integer)
    neuroticism  = db.Column(db.Integer)
    openness = db.Column(db.Integer)
    consciousness = db.Column(db.Integer)
    friendly = db.Column(db.Integer)

    city = db.Column(db.String)
    country = db.Column(db.String)
    dob = db.Column(db.Date)
    education = db.Column(db.String)
    email = db.Column(db.String)
    family = db.Column(db.String)
    gender = db.Column(db.String)
    nationality = db.Column(db.String)
    sendEmail = db.Column(db.Boolean)
    work = db.String

    def __init__(self, extraversion, neuroticism, openness, consciousness, friendly,
                 city, country, dob, education, email, gender, nationality, family = None, work = None, sendEmail = False):
        self.extraversion = extraversion
        self.neuroticism = neuroticism
        self.openness = openness
        self.consciousness = consciousness
        self.friendly = friendly

        self.dob = dob
        self.gender = gender
        self.nationality = nationality
        self.education = education
        self.family = family
        self.work = work
        self.city = city
        self.country = country
        self.email = email

    def calculate_results(self):
        return [{"title": 'extraversion', "subtitle": "bla bla", "text": "bla bla"},
         {"title": "neuroticism", "subtitle": "zaebal etet test", "text": "bla bla"}]


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



'''class VoterModel(db.Model):

    __tablename__ = 'voters'

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    patronym = db.Column(db.String)
    voting_place = db.Column(db.Text)

    def __init__(self, first_name, last_name, patronym, voting_place):
        self.first_name = first_name
        self.last_name = last_name
        self.patronym = patronym
        self.voting_place = voting_place

    @classmethod
    def find_by_f_l_name(cls, first_name, last_name):
        first_name = first_name.upper()
        last_name = last_name.upper()
        return cls.query.filter_by(first_name = first_name).filter_by(last_name = last_name)

    def json(self):
        return {"voting_place" : self.voting_place}'''