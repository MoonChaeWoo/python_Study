import sqlite3
from libs.db.db import getConn

def select_C():
    conn = getConn()
    cur = conn.cursor()

    sql='select * from test'
    cur.execute(sql)
     

    print('전체 데이터 출력하기')

    # 이처럼 위에서 fetchall()로 한번 데이터를 받았다면 밑에서 fetchall()로 연속으로 조회는 되지않는다.
    # cursor문을 사용해서 다시한번 더 받아야 가능함.
    #print(li.fetchall())
    rs = cur.fetchall()

    print('-'*10)
    for i in rs:
       print(i)
    print('-'*10)
       

    # select처럼 DB에 변화는 없고 조회만 했을 경우에는 DB연결만 닫아준다.
    #conn.commit()
    conn.close()

def select_B(num, name):
    conn = getConn()
    cur = conn.cursor()

    sql = 'select * from test where name= ?'
    # python에서 튜플에 값이 하나밖에 없을 땐 아래와 같이 (value,) 이렇게 빈 공간을 두어야한다.
    # 값이 2개 이상부터는 빈 공간을 두면 안됀다. (value, value)
    val = (name,)
    cur.execute(sql, val)

    print('fetchmany를 이용한 특정갯수만큼 데이터 가져오기')

   # 커서의 fetchall() 메서드는 모든 데이타를 한꺼번에 클라이언트로 가져올 때 사용된다.
   # 또다른 fetch 메서드로서 fetchone()은 한번 호출에 하나의 Row 만을 가져올 때 사용된다. 
   # fetchone()을 여러 번 호출하면, 호출 때 마다 한 Row 씩 데이타를 가져오게 된다. 
   # 그리고 fetchmany(n) 메서드는 n개 만큼의 데이타를 한꺼번에 가져올 때 사용된다.
    rs= cur.fetchmany(num)

    for i in rs:
        print(i)

    conn.close()


if __name__=='__main__':
    select_B(1, '홍길동')