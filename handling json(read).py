import json

with open('C:/pythonTest/python_jsonTest.json', 'r') as file_data:
    data = json.load(file_data)
# print하면 안에 있는 내용들이 리스트 형식 안의 json이 있는 형태로 출력이 된다.
print(data)

# for 문을 이용하여 data 리스트 안에 있는 값을 하나씩 뽑아서 json형태를 볼 수 있다
# 딕셔너리의 키와 값을 얻기 위해서는 items()함수를 사용하면 키와 값의 쌍을 얻을 수 있다.
# info처럼 딕셔너리 형태({'name': '홍길동', 'kor': 90, 'eng': 91, 'math': 92})인 것들에 적용시킬 수 있다.
for info in data:
    for k, v in info.items():
        print(k, v)
    print('-'*20)