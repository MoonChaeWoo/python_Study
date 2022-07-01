num = [11,22,33,44,55,66,77,88,99]
print(num)

#remove()를 사용하여 22를 삭제 remove는 값으로 삭제
num.remove(22)
print(num)

# del을 이용하여 33을 삭제 del은 인덱스 번호로 삭제 
del num[1]
print(num)

# append를 이용하여 값을 추가
num.append(22)
print(num)

# insert를 이용하여 값을 추가
num.insert(2, 33)
print(num)

# sort를 사용하여 값 정렬하기
num.sort()
print(num)

# reverse()를 사용하여 값 뒤집기
num.reverse()
print(num)

# reverse()를 이용하여 한더 더 뒤집기 즉 정렬이 아닌 그냥 뒤집기 역할
num.reverse()
print(num)

# sort(revers=true)를 사용하여 정렬과 동시에 뒤집기
num.sort(reverse=True)
print(num)

#pop를 사용하여 값을 빼오는 동시에 리스트에서 삭제하기
# pop()함수에 아무것도 안써주면, 리스트의 맨 뒤에 저장되어 있는 값을 반환하면서, 리스트에서 삭제한다.
# pop()함수에 인덱스 숫자를 적어주면, 해당 인덱스에 위치한 값을, 리스트에서 삭제하면서, 그 값을 반환한다.
print(num.pop())
print(num)

print(num.pop(4))
print(num)

