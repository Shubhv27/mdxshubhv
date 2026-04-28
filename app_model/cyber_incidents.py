import pandas as pd
import sqlite3

def migrate_cyber_incidents():
    conn = sqlite3.connect('data/users.db', check_same_thread=False)

    data = pd.read_csv('data/cyber_incidents.csv')
    data.to_sql('cyber_incidents', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()


def get_all_cyber_incidents():
    conn = sqlite3.connect('data/users.db', check_same_thread=False)
    sql = '''SELECT * FROM cyber_incidents'''
    data = pd.read_sql_query(sql, conn)

    conn.close()
    return data