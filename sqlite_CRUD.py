import sqlite3
from libs.db.db import getConn
 
class Db:
    conn = sqlite3.connect('C:/pythonTest/sqlite3/UseOfDb.db')
    cur = conn.cursor()

# db 생성
    def create_table(self):
        self.sql = "SELECT COUNT(*) FROM sqlite_master WHERE name='UseOfDB';"
        if(Db.cur.execute(self.sql)):
            print('Exist db_table')

        else:
            Db.cur.execute('''
            create table UseOfDB(name text, no text)
            ''')
            print('success create table')

# db 리스트 출력
    def list_db(self):
        self.sql = 'select * from UseOfDb'
        for k, v in Db.cur.execute(self.sql).fetchall():
            print(f'테이블의 name : {k}, no의 값 : {v}')
            print('-'*10)

# db 삽입
    def insert_db(self, name, no):
        self.sql = 'insert into UseOfDb values(?,?)'
        self.val = (self.name, self.no)
        Db.cur.execute(sql, self.val)

# db 선택
    def select_db(self, value):
        self.sql = 'select * from UseOfDb where name=?'
        self.val = (value, )
        Db.cur.execute(self.sql, self.val)
        print(Db.cur.fetchall())

# db 삭제
    def delete_db(self, value):
        self.sql = 'delete from UseOfDb where name=?'
        self.val = (self.value,)
        Db.cur.execute(sql, val)

# db 수정
    def update_db(self, origin_name, change_name):
        self.sql = 'update UseOfDb set name=? where name=?'
        self.val = (self.change_name, self.origin_name)
        Db.cur.execute(sql, val)

# db 되돌리기
    def rollback_db(self):
        Db.conn.rollback()

# db commit close
    def db_commit_close(self):
        Db.conn.commit()
        Db.conn.close()

def main():
    d = Db()

    while(True):
        select = int(input('1.전체조회 2.조회 3.등록 4.삭제 5.수정 6.작업 초기화 7.종료 : '))

        if select == 1:
            d.list_db()
        elif select == 2:
            name = input('검색을 원하는 이름을 입력 : ')
            d.select_db(name)
        elif select == 3:
            name, no = input('name과 no를 입력 : ').split()
            d.insert_db(name, no)
        elif select == 4:
            name = input('삭제 원하는 name을 입력 : ')
            d.delete_db(name)
        elif select == 5:
            name, ch_name = input('수정을 원하는 name과 바꿀 name값 입력 : ').split()
            d.update_db(name, ch_name)
        elif select == 6:
            d.rollback_db()
        elif select == 7:
            break
        else:
            print('없는 메뉴')

    d.db_commit_close()

if __name__=='__main__':
    main()