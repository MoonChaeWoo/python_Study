import sqlite
from libs.db.db import getConn

def update_A(originVal, changeVal):
    conn = getConn()
    cur = conn.cursor()

    sql = 'UPDATE test set name=? where name=?'
    val = (changeVal, originVal)
    cur.execute(sql, val)

    conn.commit()
    conn.close()

if __name__=='__main__':
    update_A('이몽룡', '이몽륭')