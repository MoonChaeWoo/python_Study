class Sj:
    def __init__(self):
        self.kor=90
        # 변수 앞에 '__'를 작성하면 private 속성이 되어 클래스 내부에서만 접근이 가능하다.
        self.__eng=75
        self.math=80
    
    # 접근을 할 수 없는 변수에 대하여  getter를 생성하여 값을 return한다.
    def get_eng(self):
        return self.__eng

    def set_eng(self, eng):
        self.__eng = eng

s1 = Sj()
#print(s1.eng)
# __때문에 값에 직접적으로 접근이 불가하여 getter에서 값을 얻는다.
print(s1.get_eng())

# setter를 이용하여 값을 포맷해준다.
s1.set_eng(95)
# setter로부터 변경된 값을 출력
print(s1.get_eng())