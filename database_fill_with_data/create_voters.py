import pandas as pd
from sqlalchemy import create_engine

#engine = create_engine('sqlite:///../data.db', echo=False)


def parse_excel_presidential(excel_path):
    df = pd.read_excel(excel_path)
    df = df[df['Names'] != 'Names']
    df_uulu = df[df['Names'].str.contains('УУЛУ|КЫЗЫ')]
    df_not_uulu = df[~df['Names'].str.contains('УУЛУ|КЫЗЫ')]

    first_name = []
    last_name = []
    patronym = []

    for name in df_not_uulu['Names']:
        name = name.split()
        if len(name) <= 2:
            first_name.append(name[1])
            last_name.append(name[0])
            patronym.append('')
        else:
            first_name.append(name[1])
            last_name.append(name[0])
            patronym.append(name[2])

    first_name = pd.DataFrame({"firstname": first_name})
    last_name = pd.DataFrame({"lastname": last_name})
    patronym = pd.DataFrame({"patronym": patronym})

    not_uulu_dataframe = pd.concat([first_name, last_name, patronym,
                                df_not_uulu['BDAY'].reset_index(), df_not_uulu['UIK_address'].reset_index()], axis=1)

    first_name = []
    last_name = []
    for name in df_uulu['Names']:
        name = name.split()
        first_name.append(name[0])
        last_name.append(name[1] + ' ' + name[2])

    first_name = pd.DataFrame({"firstname": first_name})
    last_name = pd.DataFrame({"lastname": last_name})
    patronym = pd.DataFrame({"patronym": [''] * len(first_name)})

    uulu_dataframe = pd.concat([first_name, last_name, patronym,
                                df_uulu['BDAY'].reset_index(), df_uulu['UIK_address'].reset_index()], axis=1)

    return pd.concat([not_uulu_dataframe, uulu_dataframe], axis = 0).drop('index', axis = 1).rename(index=str, columns={"BDAY": "birthday", "UIK_address": "voting_place"})
    #return not_uulu_dataframe, uulu_dataframe

def parse_excel_parliamentary(excel_path):
    df = pd.read_excel(excel_path, header = 1)
    df = df[df['Names'] != 'Names']
    df_uulu = df[df['Names'].str.contains('УУЛУ|КЫЗЫ')]
    df_not_uulu = df[~df['Names'].str.contains('УУЛУ|КЫЗЫ')]

    first_name = []
    last_name = []
    patronym = []

    for name in df_not_uulu['Names']:
        name = name.split()
        if len(name) <= 2:
            first_name.append(name[1])
            last_name.append(name[0])
            patronym.append('')
        else:
            first_name.append(name[1])
            last_name.append(name[0])
            patronym.append(name[2])

    first_name = pd.DataFrame({"firstname": first_name})
    last_name = pd.DataFrame({"lastname": last_name})
    patronym = pd.DataFrame({"patronym": patronym})

    not_uulu_dataframe = pd.concat([first_name, last_name, patronym,
                                    df_not_uulu['BDAY'].reset_index(), df_not_uulu['UIK_address'].reset_index()], axis=1)

    first_name = []
    last_name = []
    patronym = []
    for name in df_uulu['Names']:
        name = name.split()
        first_name.append(name[0])
        last_name.append(name[1] + ' ' + name[2])

    first_name = pd.DataFrame({"firstname": first_name})
    last_name = pd.DataFrame({"lastname": last_name})
    patronym = pd.DataFrame({"patronym": [''] * len(first_name)})

    uulu_dataframe = pd.concat([first_name, last_name, patronym,
                                df_uulu['BDAY'].reset_index(), df_uulu['UIK_address'].reset_index()], axis=1)

    return not_uulu_dataframe, uulu_dataframe

parl_u, parl_nu = parse_excel_parliamentary('elections/Parliamentary/Parliamentary.xlsx')



#results = parse_excel_presidential('elections/Presidential/MID.xlsx')
#results.to_sql('voters', con=engine, if_exists='append', index=False)
