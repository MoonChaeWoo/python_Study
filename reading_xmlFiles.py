import xml.etree.ElementTree as ET

# import와 from의 차이

# import
# - os 모듈을 불러오는 것

# from
# - os 모듈로부터 모두(*) import 

# import만 사용하면 모듈 안의 함수를 사용할 때, 모듈명.함수명()으로 하고
# from을 사용하면 바로 함수명()으로 사용이 가능하다.


# 파일을 읽어오기
# 파일을 읽기위해서는 

tree = ET.parse('C:/pythonTest/xmlTest.xml')

# getroot()를 사용해야 root를 가져올 수 있다.
root = tree.getroot()
print(f'root = {root}') # 현재처럼 가져오면 객체 형식으로 불러와진다.
print(f'root.tag = {root.tag}') # tag를 붙여주어야 객체형식이 아닌 root 태그 이름이 불러와진다.

# for문을 이용하여 root의 태그와 text값을 가져올 수 있다.
for i in root:
    print(i.tag, i.text)