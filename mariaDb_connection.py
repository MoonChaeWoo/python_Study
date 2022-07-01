# from libs.db.mdb 에서 만들었던 maridb 커넥터를 import 해준다.
from libs.db.mdb import getConn

# 연결이 잘 되는지 print()로 출력을 거친다.
def connect_db():
    conn = getConn()
    print(conn)

if __name__=='__main__':
    connect_db()

