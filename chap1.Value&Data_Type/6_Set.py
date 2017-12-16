#6. 집합 자료형 : 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형
#특징 : 1) 중복허용 no> 자료형의 중복을 제저하기 위한 필터로 사용  2) 순서 없음 <> 라스트, 튜플 
s1 = set([1,2,3])
print('s1: ', s1)
l1 = list(s1)
print('l1', l1)
t1 = tuple(s1)
print('t1', t1)

#1) 집합 자료형 활용하는 방법 > 교집합, 합집합, 차집합 
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print('s1&s2: ', s1&s2)  #교집합 &
print('s1.intersection(s2): ',s1.intersection(s2))  #교집합 함수 
print('s1|s2: ', s1|s2)   #합집합 |
print('s1.union(s2): ', s1.union(s2))  
print('s1-s2: ', s1-s2)   #차집합 -
print('s1.difference(s2): ',s1.difference(s2))

#2) 집합 자료형 관련 함수들 
#- 값 1개 추가하기 (add)
s1 = set([1,2,3])
s1.add(4)
print('s1: ',s1)

#-여러 값 추가하기 (update)
s1= set([1,2,3])
s1.update([4,5,6])
print('s1', s1)

#- 특정값 제거하기 (remove)
s1= set([1,2,3])
s1.remove(2)
print('s1', s1)









