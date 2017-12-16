#8. 자료형의 값을 저장하는 공간, 변수
from copy import copy
a = 3  # a는 3 객체가 저장된 메모리의 위치를 가리킨다. / 3이 메모리에 생성됨!
b= 3 # 같은 값을 참조함!


#변수를 만드는 여러가지 방법
a,b =('jung','love')
print(a)
print(b)
c = d = 'python'
print(c)

# 메모리에 생성된 변수 없애기 : del(a)
# 리스트를 변수에 넣고 복사할 때
a = [1,2,3]
b=a  #같은 값을 참조하게 바뀜 그래서 a만 변경해도 같이 변경함 
a[1] = 4
print(a)
print(b)

#참조값을 복사하지 않는 법 1
a = [1,2,3]
b =a[:]
a[1] =4
print(a)
print(b)
#참조값을 복사하지 않는 법 2: copy모듈 이용
b= copy(a)
print('b is a: ', b is a)