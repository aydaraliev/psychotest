import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///../data.db', echo=False)

#creating test
test = pd.DataFrame({'name': ["'Большая пятерка' личностных качеств"]})
test.to_sql('tests', con=engine, if_exists='append', index = False)

file = open('personality_feedback_test/questions.txt')

ru_words = []
kg_words = []
test_id = []
question_number = []

for line in file:
    line = line.strip()
    line = line.split('_')
    ru_words.append(line[1])
    kg_words.append('')
    test_id.append(1)
    question_number.append(line[0])

questions = pd.DataFrame({'ru_words': ru_words, 'kg_words': kg_words, 'test_id': test_id, 'question_number': question_number})
questions.to_sql('questions', con=engine, if_exists='append', index = False)


file.close()