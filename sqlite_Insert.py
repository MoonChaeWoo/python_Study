import sqlite3
from libs.db.db import getConn
def insert_B():
    # DB에 연결
    conn = getConn()

    # 마우스 커서 개념 DB를 조종하는 객체
    cur = conn.cursor()

    # sql은 insert 문을 사용해서 넣는데 그때 대칭되는 곳에는 ?를 넣는다..
    sql = 'INSERT INTO test VALUES(?, ?, ?, ?)'
    # val = ('마이콜', 80, 70, 60)
    val = [('마이콜', 80, 70, 60), ('둘리', 50, 40, 30), ('또치', 30, 40, 50), ('도우너', 15, 25, 35)]
    
    # cur.execute(sql, val)
    # 리스트 즉 다수의 값을 한번에 넣을 땐 executemany 함수를 사용하면 이처럼 리스트 형식을 한번에 넣는다.
    cur.executemany(sql, val)

    conn.commit()
    conn.close()

def insert_C():
    conn = getConn()
    cur = conn.cursor()

    cur.execute('''
        insert into test values('이몽룡', 50, 40, 30)
    ''')

    conn.commit()
    conn.close()


if __name__=='__main__':
    insert_B()