import sqlite3,os

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT \
        )")
    
    conn.commit()
conn.close()

path = "C:\\Drill2\\drill_files\\"
dir = os.listdir(path)

for file in dir:
        ext = os.path.splitext(file)[-1].lower()
        if ext == '.txt':
            conn = sqlite3.connect('drill.db')
            with conn:
                cur = conn.cursor()
                cur.execute('INSERT INTO tbl_files(col_name) VALUES(?)', \
                           (file,))
                conn.commit()
            conn.close
            
            print(os.path.join(file," is a txt file."))
