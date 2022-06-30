class Person:
    def __init__(self):
        self.name='홍길동'
        self.age=25

    def say():
        pass
# pass 구문은 일부 코드가 구문상 필요는 하지만 프로그램이 아무 작업도 하지 않기를
# 원하는 경우에 사용하게 됩니다.
# pass를 사용하게 되면 내부 구현이 없다 하더라도 따로 에러를 발생시키지 않고,
# 함수나 클래스를 선언할 수 있습니다.
# pass 사용법
# 1. 빈 껍데기 클래스가 필요한 경우 pass를 사용한다.

# 2. 추상 클래스에서 추상메소드(함수)를 만들 때 사용하게 된다.
# class CarBase(metaclass=ABCMeta):
     # 추상 메서드는 사용할 일이 없으니 내부 동작은 pass하고, 메서드의 존재만 알려줍니다.
#     @abstractmethod
#     def open_door(self):
#         pass

#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass


# 상속하는 방법은 자식클래스 파라미터에 부모클래스의 명을 넣어주면 상속에 이뤄진다.
class Korean(Person):
    def __init__(self):
        # 자식 클래스에서 __init__ 를 사용하여 변수를 추가하고 싶을 경우
        # super().__init__()를 넣지 않으면 부모클래스의 name, age 값들을 
        # 인식하지를 못한다. 즉 다시 초기화가 되는 듯 하다. 그러므로 super로 넣는 듯 하다.
        super().__init__()
        self.name ='한국인'
        self.lang='한국어'

    def say(self):
        return '안녕하세요'

class American(Person):
    def __init__(self):
        super().__init__()
        self.name='미국인'
        self.lang='영어'

    def say(self):
        return'Hello World!'
        

p1 = Person()
print(p1.name, p1.age)

print('------------')
k1 = Korean()
print(k1.name, k1.age, k1.lang)
print(f'{k1.name} : {k1.say()}')
print('------------')
a1 = American()
print(a1.name, a1.age, a1.lang)
print(f'{a1.name} : {a1.say()}')