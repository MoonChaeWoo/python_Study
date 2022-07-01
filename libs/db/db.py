import sqlite3

# 테이블을 만들기 전에 connection을 만들어야한다.
def getConn():
    # db에 접속하는 부분
    # sqlite3.connect('db파일의 경로') 없다면 생성해준다. 
    conn = sqlite3.connect('C:/pythonTest/sqlite3/test.db')
    # conn은 db접속에 대한 정보를 가지고 있으므로  return해준다.
    # 그럼 다른 곳에서 db에 접속하려고 할 때 마다 getConn()을 사용한다면
    # db에 쉽게 접근 할 수 있다.
    return conn

