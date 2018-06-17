from db import db
from models.interpretation import InterpretationModel


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
    dob = db.Column(db.String)
    education = db.Column(db.String)
    email = db.Column(db.String)
    family = db.Column(db.String)
    gender = db.Column(db.String)
    nationality = db.Column(db.String)
    sendEmail = db.Column(db.Boolean)
    work = db.Column(db.String)

    responses = db.Column(db.String)
    uuid4 = db.Column(db.String)
    ru_language = db.Column(db.Boolean)

    def __init__(self, extraversion, neuroticism, openness, consciousness, friendly,
                 city, country, dob, education, email, gender, nationality,
                 responses, uuid4, family=None, work=None, sendEmail=False, ru_language=False):
        self.extraversion = extraversion
        self.neuroticism = neuroticism
        self.openness = openness
        self.consciousness = consciousness
        self.friendly = friendly

        self.responses = responses
        self.uuid4 = uuid4

        self.dob = dob
        self.gender = gender
        self.nationality = nationality
        self.education = education
        self.family = family
        self.work = work
        self.city = city
        self.country = country
        self.email = email
        self.sendEmail = sendEmail
        self.ru_language = ru_language

    def calculate_results(self):
        results = []
        def calculate_char(current_char):
            score_for_current_char = getattr(self, current_char)
            if 0 <= score_for_current_char < 21:
                return InterpretationModel.return_characteristic(character=current_char, line_num=1)
            elif 21 <= score_for_current_char < 42:
                print(2)
                return InterpretationModel.return_characteristic(character=current_char, line_num=2)
            elif 42 <= score_for_current_char < 60:
                print(3)
                return InterpretationModel.return_characteristic(character=current_char, line_num=3)
            elif 60 <= score_for_current_char < 85:
                print(4)
                return InterpretationModel.return_characteristic(character=current_char, line_num=4)
            elif 85 <=  score_for_current_char <= 100:
                print(5)
                return InterpretationModel.return_characteristic(character=current_char, line_num=5)


        for character in ["extraversion", "neuroticism", "openness", "consciousness", "friendly"]:
            results.append(calculate_char(character))


        return results

        #[{"title": 'extraversion', "subtitle": "bla bla", "text": "bla bla"},
        #{"title": "neuroticism", "subtitle": "zaebal etot test", "text": "bla bla"}]

    def to_dict(self):
        return {"uuid4": self.uuid4, "responses": self.responses, "extraversion": self.extraversion,
                "neuroticism": self.neuroticism, "openness": self.openness, "conciousness": self.consciousness,
                "friendly": self.friendly, "birthday": self.dob, "gender": self.gender,
                "nationality": self.nationality, "education": self.education, "family": self.family,
                "work": self.work, "city": self.city, "country": self.country, "email": self.email,
                "send_email": self.sendEmail, "test_in_russian": self.ru_language}


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