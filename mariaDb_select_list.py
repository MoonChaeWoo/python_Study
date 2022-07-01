from libs.db.mdb import getConn

def select_db():
    conn = getConn()
    cur = conn.cursor()

    sql = 'select * from pydb'
    cur.execute(sql)

    for k, c,v,b in cur.fetchall():
        print(k, c ,v, b)
        # 값을 하나도로 가져올 수 있음

    conn.commit()
    conn.close()

if __name__=='__main__':
    select_db()