class Person:
    li = []

    def __init__(self, sp):
        # self를 사용하면 각각의 객체들의 값을 갖게된다.
        # self.li = []
        # self.li.append(sp)

        # 클래스 변수는 각각의 객체들이 공유를 하는 값이된다.
        # 클래스 변수는 변수 앞에 클래스 이름을 넣어주면 된다.
        Person.li.append(sp)

    def disp(self):
        print(f'li의 리스트 값은 {self.li}이다')

p1=Person('우유')
p1.disp()
p2=Person('콜라')
p2.disp()
p3=Person('쥬스')
p3.disp()


