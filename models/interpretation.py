from db import db

class InterpretationModel(db.Model):

    __tablename__ = 'interpretation'

    id = db.Column(db.Integer, primary_key=True)

    extraversion_title = db.Column(db.Text)
    extraversion_ru = db.Column(db.Text)
    extraversion_kg = db.Column(db.Text)

    neuroticism_title = db.Column(db.Text)
    neuroticism_ru = db.Column(db.Text)
    neuroticism_kg = db.Column(db.Text)

    openness_title = db.Column(db.Text)
    openness_ru = db.Column(db.Text)
    openness_kg = db.Column(db.Text)

    consciousness_title = db.Column(db.Text)
    consciousness_ru = db.Column(db.Text)
    consciousness_kg = db.Column(db.Text)

    friendly_title = db.Column(db.Text)
    friendly_ru = db.Column(db.Text)
    friendly_kg = db.Column(db.Text)

    def __init__(self, extraversion_title, extraversion_ru, extraversion_kg, neuroticism_title,
                 neuroticism_ru, neuroticism_kg, openness_title, openness_ru, openness_kg, consciousness_title,
                 consciousness_ru, consciousness_kg, friendly_title, friendly_ru, friendly_kg):

        self.extraversion_title = extraversion_title
        self.extraversion_ru = extraversion_ru
        self.extraversion_kg = extraversion_kg

        self.neuroticism_title = neuroticism_title
        self.neuroticism_ru = neuroticism_ru
        self.neuroticism_kg = neuroticism_kg

        self.openness_tile = openness_title
        self.openness_ru = openness_ru
        self.openness_kg = openness_kg

        self.consciousness_title = consciousness_title
        self.consciousness_ru = consciousness_ru
        self.consciousness_kg = consciousness_kg

        self.friendly_title = friendly_title
        self.friendly_ru = friendly_ru
        self.friendly_kg = friendly_kg

    @classmethod
    def return_characteristic(cls, character, line_num):
        needed_row = cls.query.filter_by(id=line_num).first()
        if character == "extraversion":
            return {"title": character, "subtitle": needed_row.extraversion_title,
                    "text": needed_row.extraversion_ru, "text_kg": needed_row.extraversion_kg}
        elif character == "neuroticism":
            return {"title": character, "subtitle": needed_row.neuroticism_title,
                    "text": needed_row.neuroticism_ru, "text_kg": needed_row.neuroticism_kg}
        elif character == "openness":
            return {"title": character, "subtitle": needed_row.openness_title,
                    "text": needed_row.openness_ru, "text_kg": needed_row.openness_kg}
        elif character == "consciousness":
            return {"title": character, "subtitle": needed_row.consciousness_title,
                    "text": needed_row.consciousness_ru, "text_kg": needed_row.consciousness_kg}
        elif character == "friendly":
            return {"title": character, "subtitle": needed_row.friendly_title,
                    "text": needed_row.friendly_ru, "text_kg": needed_row.friendly_kg}
        else:
            raise ValueError("Character should match one of the 5 characteristics!(extraversion, neuroticism etc...)")


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()