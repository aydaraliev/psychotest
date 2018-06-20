import pandas as pd
from sqlalchemy import create_engine
import os


engine = create_engine('sqlite:///../data.db', echo=False)


def parse_excel_presidential(excel_path):
    df = pd.read_excel(excel_path)
    df = df[df['Names'] != 'Names']
    df_uulu = df[df['Names'].str.contains(' УУЛУ | КЫЗЫ ')]
    df_not_uulu = df[~df['Names'].str.contains(' УУЛУ | КЫЗЫ ')]

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

    parliamentary = [False] * len(first_name)
    presidential = [True] * len(last_name)

    first_name = pd.DataFrame({"firstname": first_name})
    last_name = pd.DataFrame({"lastname": last_name})
    patronym = pd.DataFrame({"patronym": patronym})
    parliamentary = pd.DataFrame({"parliamentary": parliamentary})
    presidential = pd.DataFrame({'presidential': presidential})

    not_uulu_dataframe = pd.concat([first_name, last_name, patronym,
                                    df_not_uulu['BDAY'].reset_index(), df_not_uulu['UIK_address'].reset_index(),
                                    presidential, parliamentary], axis=1)

    first_name = []
    last_name = []

    for name in df_uulu['Names']:
        name = name.split()
        first_name.append(name[2])
        last_name.append(name[0] + ' ' + name[1])

    parliamentary = [False] * len(first_name)
    presidential = [True] * len(last_name)

    first_name = pd.DataFrame({"firstname": first_name})
    last_name = pd.DataFrame({"lastname": last_name})
    patronym = pd.DataFrame({"patronym": [''] * len(first_name)})
    parliamentary = pd.DataFrame({"parliamentary": parliamentary})
    presidential = pd.DataFrame({'presidential': presidential})

    uulu_dataframe = pd.concat([first_name, last_name, patronym,
                                df_uulu['BDAY'].reset_index(), df_uulu['UIK_address'].reset_index(),
                                presidential, parliamentary], axis=1)

    return pd.concat([not_uulu_dataframe, uulu_dataframe],
                     axis=0).drop('index', axis=1).rename(index=str,
                                                          columns={"BDAY": "birthday", "UIK_address": "voting_place"})
    # return not_uulu_dataframe, uulu_dataframe


def parse_excel_parliamentary(excel_path):
    df = pd.read_excel(excel_path, header=1)
    df = df[df['Names'] != 'Names']
    df_uulu = df[df['Names'].str.contains(' УУЛУ | КЫЗЫ ')]
    df_not_uulu = df[~df['Names'].str.contains(' УУЛУ | КЫЗЫ ')]

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

    parliamentary = [True] * len(first_name)
    presidential = [False] * len(last_name)

    first_name = pd.DataFrame({"firstname": first_name})
    last_name = pd.DataFrame({"lastname": last_name})
    patronym = pd.DataFrame({"patronym": patronym})
    parliamentary = pd.DataFrame({"parliamentary": parliamentary})
    presidential = pd.DataFrame({'presidential': presidential})

    not_uulu_dataframe = pd.concat([first_name, last_name, patronym,
                                    df_not_uulu['BDAY'].reset_index(), df_not_uulu['UIK_address'].reset_index(),
                                    presidential, parliamentary], axis=1)

    first_name = []
    last_name = []

    for name in df_uulu['Names']:
        name = name.split()
        first_name.append(name[2])
        last_name.append(name[0] + ' ' + name[1])

    parliamentary = [True] * len(first_name)
    presidential = [False] * len(last_name)

    first_name = pd.DataFrame({"firstname": first_name})
    last_name = pd.DataFrame({"lastname": last_name})
    patronym = pd.DataFrame({"patronym": [''] * len(first_name)})
    parliamentary = pd.DataFrame({"parliamentary": parliamentary})
    presidential = pd.DataFrame({'presidential': presidential})


    uulu_dataframe = pd.concat([first_name, last_name, patronym,
                                df_uulu['BDAY'].reset_index(), df_uulu['UIK_address'].reset_index(),
                                presidential, parliamentary], axis=1)

    return pd.concat([not_uulu_dataframe, uulu_dataframe],
                     axis=0).drop('index', axis=1).rename(index=str,
                                                          columns={"BDAY": "birthday", "UIK_address": "voting_place"})


#parl_u, parl_nu = parse_excel_parliamentary('elections/Parliamentary/Parliamentary.xlsx')

if __name__ == '__main__':
    # pres = parse_excel_presidential('elections/Presidential/test_data_pres.xlsx')
    # parl = parse_excel_parliamentary('elections/Parliamentary/test_data_parl.xlsx')
    # to_db = pd.concat([pres,parl], axis=0)
    # to_db.sort_values(['firstname', "lastname"]).reset_index(drop=True)
    # to_db.to_sql('voters', con=engine, if_exists='append', index=False)

    presidential = []
    parliamentary = []
    for file in os.listdir('elections/Presidential/'):
        presidential.append(parse_excel_presidential('elections/Presidential/'+file))
    for file in os.listdir('elections/Parliamentary'):
        parliamentary.append(parse_excel_parliamentary('elections/Parliamentary/' + file))

    presidential = pd.concat(presidential, axis=0)
    parliamentary = pd.concat(parliamentary, axis=0)
    to_db = pd.concat([presidential, parliamentary], axis=0)
    to_db.sort_values(['firstname', 'lastname']).reset_index(drop=True)
    to_db.to_sql('voters', con=engine, if_exists='append', index=False, chunksize=10000)

#results = parse_excel_presidential('elections/Presidential/MID.xlsx')
#results.to_sql('voters', con=engine, if_exists='append', index=False)
#results = parse_excel_parliamentary('elections/Parliamentary/Parliamentary.xlsx')
#results.to_sql('voters', con=engine, if_exists='append', index=False, chunksize=10000)
