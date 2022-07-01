from libs.db.mdb import getConn

def search_value(value):
    conn = getConn()
    cur = conn.cursor()

    sql = 'select * from pydb where name like %s'
    val = (value,)

    # like는 문자를 비교할 때 쓰인다.
    # %는 모든 문자를 말한다.
    # ex) %길동% = 길동이 포함된 아이템
    # ex) %길동 = 마지막에 길동이 포함된 아이템
    # ex) 길동% = 시작하는 부분에 길동이 포함된 아이템
    # _는 한글자를 말한다.
    # ex) _길동_ = 길동이라는 글자 앞뒤로 한글자씩 포함된 아이템
    # ex) _길동 = 마지막에 길동이 포함되며 길동의 앞글자는 딱 하나여야함 아이템
    # ex) 길동% = 시작하는 부분에 길동이며 길동의 마지막 부분은 한글자 밖에 없는 아이템

    cur.execute(sql, val)

    rs = cur.fetchall()
    print(rs)

    conn.commit()
    conn.close()

if __name__=='__main__':
    search_value('홍길동')