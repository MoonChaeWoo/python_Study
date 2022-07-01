# pip install mysql-connector-python을 먼저 설치를 한다.
# 그 후 mysql.connector를 import를 해준다.
import mysql.connector as mdb
# import후 실행을 하고 오류가 있는지 확인한다.

# db에 접속하려면 db의 접속 정보가 필요하므로 여기서 작성한다.
# 아래와 같이 5가지의 정보가 필요하다.
config={
    'user' : 'root',
    'password' : '0000',
    'host' : '127.0.0.1',
    'database' : 'pythondb',
    'port' : '3306'
}

# connection을 넘겨주는 함수를 생성한다.
def getConn():
    # connect(**config) 위에서 만든 config를 넣어줄 가변인자 방식으로 넣어준다.

    # 가변 인자
    conn = mdb.connect(**config)
    return conn