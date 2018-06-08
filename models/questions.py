from db import db


class QuestionModel(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    ru_words = db.Column(db.Text)
    kg_words = db.Column(db.Text)

    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))
    test = db.relationship('TestModel')

    def __init__(self, ru_words, kg_words, test_id):
        self.ru_words = ru_words
        self.kg_words = kg_words
        self.test_id = test_id

    def json(self):
        return {'ru_words': str(self.ru_words), 'kg_words': str(self.kg_words), 'value': None}

    @classmethod
    def find_by_id(cls, test_id):
        return cls.query.filter_by(test_id=test_id)

    @classmethod
    def find_by_ru_words(cls, ru_words):
        return cls.query.filter_by(ru_words=ru_words).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
