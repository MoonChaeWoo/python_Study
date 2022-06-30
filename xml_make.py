from xml.etree.ElementTree import *

# xml을 만들기
person=Element('Person')

# Element의 태그이름을 정해준 다음 text로 값을 넣어준다.
name=Element('name')
name.text='홍길동'
# 그후 person 태그에 추가를 해준다.
person.append(name)
# <person>
#   <name>홍길동</name>
# </person>
# 현재까지 만들어진 모습은 이렇다.

age=Element('age')
age.text='15'
person.append(age)

# 위처럼 생성 후 append 형식이 아닌 한줄로 작성하여 추가하는 방법
SubElement(person, 'address').text='대구'

# append는 가장 마지막
# insert(index, value)는 value를 해당 index에 넣어준다.
no = Element('no')
no.text='17'
person.insert(1, no)

# 특정 값을 삭제할 땐 remove()를 사용하여 제거한다.
# remove('value')로 삭제할 때 사용
# del list[index number]로 하여 삭제할 때 사용
person.remove(no)

# 태그에 속성값을 넣어줄 땐 attrib['넣을 속성이름']='넣을 속성 값'
person.attrib['data']='2022-06-30'

# 최종적으로 만든 것을 xml로 표현하겠다는게 dump이다.
dump(person)