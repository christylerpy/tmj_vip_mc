import re
import sqlite3

import settings as st

sql_db = 'tmj_sqlite.db'
sql_create_tmj_files_info = '''
    CREATE TABLE IF NOT EXISTS tmj_files_info
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    identity TEXT  NOT NULL,
    file_name TEXT UNIQUE NOT NULL,
    file_mtime DATETIME NOT NULL);
'''
sql_create_table = [f"""
    CREATE TABLE IF NOT EXISTS {d_rf['identity']}
    (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    {str.join(',', [kp + ' TEXT NOT NULL' for kp in d_rf['key_pos']])},
    {str.join(',', [vp + ' ' + vt for vp, vt in zip(d_rf['val_pos'], d_rf['val_type'])])});"""
                    for d_rf in st.DOC_REFERENCE]
sql_create_table = [re.sub(r'日期\s+TEXT', '日期 DATETIME', content) for content in sql_create_table]
sql_create_table.append(sql_create_tmj_files_info)
table_list = [item['identity'] for item in st.DOC_REFERENCE]
table_list.append('tmj_files_info')

conn = sqlite3.connect(sql_db)
cur = conn.cursor()
for create_table in sql_create_table:
    cur.execute(create_table)

# 手工处理的query写在此处
# cur.execute('drop table tmj_files_info')

conn.commit()
# cc = 1
# for table in table_list:
#     cur = cur.execute(f"select * from sqlite_master where name='{table}';")
#     for row in cur:
#         print(cc)
#         print('查询成功', row)
#         cc += 1
conn.close()


def tables_have_been_created():
    print('tables have been created in sqlite, get it done!')
