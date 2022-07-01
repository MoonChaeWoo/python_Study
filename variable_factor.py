# 가변 인자에 대하여

def variable_factor(*variable):
    # variable_factor(1,2,3,4)으로 값을 넘기면
    # (1,2,3,4)형식처럼 튜플로 넘어온다.
    print(variable)

def variable_factor2(**variable):
    # variable_factor2(a=1,b=2,c=3,d=4)으로 값을 넘기면
    # {'a': 1, 'b': 2, 'c': 3, 'd': 4} 딕셔너리 형태로 넘어온다.
    print(variable['a'])

def variable_factor3(**variable):
    # variable_factor3(**config) 값을 넘길때도 **넘긴다.
    # 딕셔너리를 그대로 받아서 딕셔너리 형태로 출력을 해준다.
    print(variable)

if __name__=='__main__':

    config={
    'user' : 'root',
    'password' : '0000',
    'host' : '127.0.0.1',
    'database' : 'pythondb',
    'port' : '3306'
    }

    variable_factor3(**config)