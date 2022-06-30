class Point:
    def __init__(self):
        self.x=int(input('x='))
        self.y=int(input('y='))

    def disp(self):
        pass

class Rect(Point):
    def __init__(self):
        super().__init__()
        self.w=int(input('w='))
        self.h=int(input('h='))

    def disp(self):
        print(f'사각형 self.x={self.x}, self.y={self.y},self.w={self.w},self.h={self.h}')

class Circle(Point):
    def __init__(self):
        super().__init__()
        self.r=int(input('r='))

    def disp(self):
        print(f'원형 self.x={self.x}, self.y={self.y},self.r={self.r}')

def main():
    pass
    li = []
    while True:
        s = int(input('1.사각형 2.원 3.조회 4.종료 : '))

        if s == 1:
            li.append(Rect())
        elif s == 2:
            li.append(Circle())
        elif s == 3:
            for i in li:
                i.disp()
        elif s == 4:
            break
        else:
            print('없는 메뉴입니다.')
            pass
    print('프로그램을 종료합니다.')

main()