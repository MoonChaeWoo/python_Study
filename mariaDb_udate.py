from libs.db.mdb import getConn

def update_db(originvalue, chagevalue):
    conn = getConn()
    cur = conn.cursor()

    sql = 'update pydb set name = %s where name like %s'
    val = (chagevalue, originvalue)
    cur.execute(sql, val)

    conn.commit()
    conn.close()

if __name__=='__main__':
    update_db('홍길동', '고길동')