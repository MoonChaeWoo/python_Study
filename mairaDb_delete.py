from libs.db.mdb import getConn

def delete_db(value):
    conn = getConn()
    cur = conn.cursor()

    sql = 'delete from pydb where name like %s'
    val = (value,)
    cur.execute(sql, val)

    conn.commit()
    conn.close()

if __name__=='__main__':
    delete_db('고길동')