import pandas as pd
from sqlalchemy import create_engine
#from app import db

def create_excel():
    engine = create_engine('sqlite:///../data.db', echo=False)
    writer = pd.ExcelWriter('../test_results/data.xlsx', engine='xlsxwriter')

    users = pd.read_sql_table('users', engine)
    searches = pd.read_sql_table('searchvoters', engine)
    found_not_found = pd.read_sql_table('found_not_found', engine)

    users.to_excel(writer, sheet_name="users", index=False)
    searches.to_excel(writer, sheet_name="searches", index=False)
    found_not_found.to_excel(writer, sheet_name="found_not_found", index=False)

    writer.save()

if __name__=="__main__":
    create_excel()