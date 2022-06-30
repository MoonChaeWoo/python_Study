import json

li = [{'name' : '홍길동', 'kor' : 90, 'eng' : 91, 'math' : 92},
{'name' : '이춘향', 'kor' : 80, 'eng' : 81, 'math' : 82},
{'name' : '이몽룡', 'kor' : 70, 'eng' : 71, 'math' : 72}]

# python에서 Json방식과 dictionary방식 사용은 같다.

with open('C:/pythonTest/python_jsonTest.json', 'w') as file_data:
    # json.dump와 json.dumps차이
    # json.dump는 python 직렬화된 객체를 Json 형식 데이터로 파일을 쓰는데 사용
    # json.dumps는 python 모든 개체를 json 형식의 string으로 인코딩한다.

    # json.dump(pythonDict, file) -> 파이썬 객체를 스트림 객체(파일 등)으로 변환한다.
    # json.dumps(pythonDict) -> 파이썬 객체를 한줄의 (직렬화된) json 문자열로 변환한다.

    # file_data에 li객체를 ensure_ascii=False 해줌으로써 한글이 깨지는걸 방지하면서 작성한다.
    json.dump(li, file_data, ensure_ascii=False)

    # json.load(data) -> data(파일 등)를 파싱해서 파이썬의 객체(dict 등)로 변환한다.
    # json.loads(data) -> json 문자열을 파싱해서 파이썬 객체로 변환해준다.

