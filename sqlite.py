from libs.db.db import getConn
# import libs.db.db.getConn as dbGet 이처럼 불러올 수 도 있다.

def create_table():
    # 이렇게 해줌으로써 db에 연결이 됨
    conn = getConn()
    # 포인터 개념으로 생각하면 된다. cursor을 가지고 db작업을 한다.
    cur = conn.cursor()
    # cursor 객체인 cur을 가지고 execute()문을 사용하여 사용하면 된다.
    # execute()안에 쿼리문을 넣어주면 된다.
    cur.execute('''
        create table test(name text, 
        kor int, 
        eng int,
        mat int)
    ''')
    # 최종적으로 connection을 반영하기 위해 commit를 해주어야한다.
    conn.commit()
    # connection을 다 사용했으면 닫아주어야한다.
    conn.close()


if __name__=='__main__':
    # 즉, import 했을 때 그 모듈안에 있는 모든 코드들이 그대로 실행되는 것을 막기 위해
    # if __name__=="__main__": 으로 메인 함수 선언을 해주어야 한다고 이해하면 될 것 같다.
    create_table()

    # DB Browser for SQLite를 사용하여 해당 db를 확인하면 생성된 파일 내용을 확인할 수 있다.