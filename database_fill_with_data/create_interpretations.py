import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../data.db', echo=False)

feedback = pd.read_excel('personality_feedback_test/Personality Feedback Rus.xlsx')

extraversion_title = pd.DataFrame({'extraversion_title': [feedback['Экстраверсия'][6] for x in range(5)]})
extraversion_ru = feedback['Экстраверсия'][0:5].rename_axis('extraversion_ru').rename('extraversion_ru')
extraversion_kg = pd.DataFrame({'extraversion_kg': ['' for x in range(5)]})

neuroticism_title = pd.DataFrame({'neuroticism_title': [feedback['Нейротизм'][6] for x in range(5)]})
neuroticism_ru = feedback['Нейротизм'][0:5].rename_axis('neuroticism_ru').rename('neuroticism_ru')
neuroticism_kg = pd.DataFrame({'neuroticism_kg': ['' for x in range(5)]})

openness_title = pd.DataFrame({'openness_title': [feedback['Открытость'][6] for x in range(5)]})
openness_ru = feedback['Открытость'][0:5].rename_axis('openness_ru').rename('openness_ru')
openness_kg = pd.DataFrame({'openness_kg': ['' for x in range(5)]})

consciousness_title = pd.DataFrame({'consciousness_title': [feedback['Сознательность'][6] for x in range(5)]})
consciousness_ru = feedback['Сознательность'][0:5].rename_axis('consciousness_ru').rename('consciousness_ru')
consciousness_kg = pd.DataFrame({'consciousness_kg': ['' for x in range(5)]})

friendly_title = pd.DataFrame({'friendly_title': [feedback['Доброжелательность'][6] for x in range(5)]})
friendly_ru = feedback['Доброжелательность'][0:5].rename_axis('friendly_ru').rename('friendly_ru')
friendly_kg = pd.DataFrame({'friendly_kg': ['' for x in range(5)]})

interpretation_table = pd.concat([extraversion_title, extraversion_ru, extraversion_kg, neuroticism_title,
                 neuroticism_ru, neuroticism_kg, openness_title, openness_ru, openness_kg, consciousness_title,
                 consciousness_ru, consciousness_kg, friendly_title, friendly_ru, friendly_kg], axis = 1)

interpretation_table.to_sql('interpretation', con=engine, if_exists='append', index = False)