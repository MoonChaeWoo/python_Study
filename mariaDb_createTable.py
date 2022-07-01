from libs.db.mdb import getConn

def create_table():
    conn = getConn()
    cur = conn.cursor()

    sql = 'create table pyDB(name varchar(20), kor int, eng int, math int)'
    cur.execute(sql)

    conn.commit()
    conn.close()


if __name__=='__main__':
    create_table()