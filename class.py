# 클래스 생성
class Person:
    # __init__는 생성자이다.
    def __init__(self, name, age):
        # 멤버 변수는 __init__에서 초기화 할 수 있다.
        self.name = name
        self.age = age

    # 클래스 내부의 함수 = 메소드라고도 한다.
    def disp(self):
        print(f'Person의 값은 {self.name}과 {self.age}')

p1=Person('홍길동', 25)
p2=Person('이춘향', 22)
print(p1.name, p2.age)
p2.disp()

# 
class Person2:
    def __init__(self):
        self.name=input('이름을 입력하세요 : ')
        self.age=int(input('나이를 입력하세요 : '))

    def disp(self):
        print(f'입력된 이름은 {self.name}이고 나이는 {self.age}입니다.')

# 인스턴스화에서 입력 값을 요한다.
inputP = Person2()
# 인스턴스화에서 받은 값을 출력해준다.
inputP.disp()

li = []
for i in range(3):
    li.append(Person2())

# li를 넣어주면 li의 값 끝까지 보여준다.
for i in li:
    i.disp()

 

