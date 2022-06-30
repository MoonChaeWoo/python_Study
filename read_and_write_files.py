# 파일을 읽고 쓰는 방법
# 1. 먼저 open()을 사용하여 파일을 열어야한다.
# 2. open('경로', '모듈 r또는 w')안에는 파일의 경로를 적어주어야한다.
# 3. 경로가 '/'로 사용할 땐 1개로 되지만 '\'를 사용할 땐 '\\' 2개를 사용해주어야 
#    오류가 없다.

# 파일열기모드: 파일열기모드란 파일을 Binary형태로 읽을지 아니면 인코딩단위로 읽을지, 파일을 읽을건지 쓸건지 아니면 동시에 할건지에 대한 부분을 정하는 지시자라고 볼 수 있습니다.

# r: 읽기 모드, 파일을 읽을 때 사용합니다.
# w: 쓰기 모드, 파일에 쓸 때 사용하며 파일이 이미 동일한 이름으로 존재한다면 덮어씁니다.
# a: 추가 모드, 존재하는 파일에 추가할 때 사용하며 파일이 없다면 생성합니다.
# r+, w+, a+: 읽기모드 + 쓰기모드, w+와 a+의 차이는 위와 같습니다.
# rb, wb, ab, rb+, wb+, ab+: 각각의 모드들은 위와 동일하나 Binary 포맷으로 읽거나 쓰는걸 진행합니다.

# 쓰기 모드는 모듈 부분에 w를 넣으면 쓰기가 된다.
f=open('C:/pythonTest/abc.txt', 'w')

for i in range(1,7):
    f.write(f'{i}번째 \n')
# 파일은 마지막에 꼭 닫아주어야 한다는 것을 잊으면 안됀다.
f.close()

# 읽기 모드 모듈 부분에 r을 넣으면 읽기가 된다.
f=open('C:/pythonTest/abc.txt', 'r')
m = f.readline() # 한줄씩 읽을 땐 readline()
m2 = f.readlines() # 한번에 다 읽을 땐 readlines()
f.close()

print(f'm = {m}')
print(f'm2 = {m2}')

# 파일을 읽을 때
# with를 함께 사용한다면 파일 입출력 단계에서 해당 파일을 위해 openk close를 해주어야하는데 
# "with open('C:/pythonTest/abc.txt', 'r') as file_data" 를 한다면 with가 자동으로 close를 불러와준다.
# print(file_data.readline(), end='')

# 파일을 쓸 때
# with open('C:/pythonTest/abc.txt', 'w') as file_data
# for i in range(1,7):
#     file_data.write(f'{i}번째 \n')