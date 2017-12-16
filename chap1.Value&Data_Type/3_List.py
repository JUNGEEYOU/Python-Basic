#3. 리스트 자료형 
a = [1,2,3]
print('a[1]: ', a[1])
print('a[-1]: ', a[-1])
b= [1,2,['a', 'b', 'c']]
print('b[-1][1]: ', b[-1][1])

#2) 리스트의 슬라이싱 
a = [1,2,3,4,5]
print('a[0:2]: ', a[0:2])
print('a[:2]: ', a[:2])
b= [1,2,['a', 'b', 'c'],4,5]
print("b[2:5]: ", b[2:5])
print("b[2][:2]: ", b[2][:2])

#3) 리스트 연산자  +/ *
a= [1,2,3]
b= [4,5,6]
print('a+b: ', a+b)
print("a*3: ", a*3)

#4) 리스트 수정, 변경과 삭제 
a =[1,2,3]
a[2] = 4 
print('a: ',a )
a[1:2] = ['a', 'b', 'c']  #a[1] = ['a', 'b', 'c'] 와는 다름!!! 이건 이차 배열로!!
print('a: ',a )
#삭제 하기 1
a[1:3] =[]
print('a: ',a )
#삭제하기 2 : del함수 이용 
del a[1]
print('a: ',a )


#5) 리스트 관련 함수들
# - 리스트에 요소 추가 (append)
a = [1,2,3]
a.append(4)  #마지막에 추가함 
print('a: ',a )
a.append([5,6])
print('a: ',a )

#-리스트 정렬(sort) 
a = [1,4,5,2]
a.sort()
print('a: ',a )
b = ['s', 'a', 'f']
b.sort()
print('b:',b)

#- 리스트 뒤집기(reverse): 리스트에서 그냥 반대로! 
a = ['s', 'a', 'f']
a.reverse()
print('a: ',a)

#- 위치 반환(index)
a= [1,2,3]
print('a.index(3)',a.index(3)) #3이 있는 위치를 출력 
#print('a.index(0)',a.index(0))  #없으니깐 오류 출력 


#-리스트에 요소 삽입 (insert)
a= [1,2,3]
a.insert(0,4)  #0번째 인덱스에 4삽입 
print('a: ', a)

#-리스트 요소 제거(remove)
a = [1,2,3,1,2,3]
a.remove(3)  #첫번째로 나오는 3 제거 
print('a: ',a )

#- 리스트 요소 끄집어내기 (POP)
a = [1,2,3]
a.pop()
print('a: ', a)

a.pop(1)   #1번째 요소 삭제 
print('a: ', a)

#-리스트에 포함된 요소 x 개수 세기(count) 
a =[1,2,3,1,1]
print('a.count(1): ', a.count(1))   

#- 리스트 확장 (extend): extend(x)에서 x는 리스트만 올수 있고 원래 a리스트에 x를 더함 
a = [1,2,3]
a.extend([4,5])
print('a: ', a)