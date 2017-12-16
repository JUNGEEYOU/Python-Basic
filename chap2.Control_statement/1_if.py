#1. if문 
#들여 쓰기는 언제나 같은 깊이로 한다!!!(space 4개로 하기)
#1) 비교 연산자 if
money =2000
if(money >=3000):
    print("택시 타고 가라")
else:
    print('걸어 가라')


#2) and, or , not  (x or y : 둘 중 하나 참이면 참 / not x : x가 거짓이면 참 )
money = 2000
card =1 
if money>=3000 or card: 
    print("택시 타고 가라")
else:
    print('걸어 가라')

#3) x in s, x not in s 
# x in (리스트/튜플/ 문자열)
pocket =['paper','cellphone', 'money']
if ('money' in pocket):
    print("택시 타고 가라")
else:
    print('걸어 가라')

# 4) 조건문에서 아무 일도 하지 않게 설정하기 (pass)
pocket =['paper','cellphone', 'money']
if ('money' in pocket):
    pass
else:
    print('걸어 가라')

#5) 다양한 조건을 판단하는 elif =else if
pocket2 =['paper','cellphone']
card2= 1;
if ('money' in pocket2):
     print("택시 타고 가라")
elif card2:
    print('택시 타고 가라')
else: 
    print('걸어 가라')

