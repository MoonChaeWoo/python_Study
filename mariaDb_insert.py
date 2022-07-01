from libs.db.mdb import getConn

def insert_mdb(name, kor, eng, math):
    conn = getConn()
    cur = conn.cursor()

    sql = 'insert into pydb values(%s,%s,%s,%s)'
    val = (name, kor, eng, math)
    cur.execute(sql, val)

    # execute와 executemany의 차이

    # - execute는 단일값에 대하여 사용된다.
    # val = (name, kor, eng, math)
    # cur.execute(sql, val)

    # executemany는 튜플 또는 리스트 또는 딕셔너리의 여러값을 받을 때 사용된다.
    
    # data = (
    # ('홍진우', 1, '서울'),
    # ('강지수', 2, '부산'),
    # ('김청진', 1, '서울'),
    # )
    # sql = """insert into customer(name,category,region)
    #         values (%s, %s, %s)"""
    # curs.executemany(sql, data)


    conn.commit()
    conn.close()

if __name__=='__main__':
    insert_mdb('홍길동', 90, 91, 92)