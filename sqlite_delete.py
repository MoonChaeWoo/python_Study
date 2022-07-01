import sqlite3
from libs.db.db import getConn

def delete_A(del_name):
    conn = getConn()
    cur = conn.cursor()

    sql='DELETE FROM test where name=?'
    val = (del_name,)
    cur.execute(sql, val)

    conn.commit()
    conn.close()

if __name__=='__main__':
    delete_A('이몽륭')