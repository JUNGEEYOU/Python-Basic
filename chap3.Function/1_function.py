#1. 함수 
def sum(a,b):
    return a+b
print("sum(1,2): ",sum(1,2))

#2) 입력값이 몇 개가 되는지 모를 때 
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum
print('sum_many(1,2,3,4,5)',sum_many(1,2,3,4,5))


#3) 함수의 결과값은 언제나 하나이다.
def sum_and_mul(a,b):
    return a+b,a*b
print('sum_and_mul(3,2):', sum_and_mul(3,2))  #튜플로 출력!!

#4) return 으로 빠져나가기 
def say_nick(nick):
    if(nick == '바보'):
        return
    print('나의 별명은 %s 입니다.'%nick)

say_nick('정이')
say_nick('바보')


#5) 입력 인수에 초깃값 미리 설정하기 
def say_myself(name, old, man =True):   #뒤에 설정하기!!!
    print('이름은 %s 입니다. '%name)
    print('나이는 %d 입니다.' %old)
    if man:
        print('남자입니다.')
    else:
        print('여자입니다.')

say_myself('정이', 23, False)
say_myself('주', 26)

#6) 스코프 
#1) return 이용하기
a =1 
def vartest(a):
    a = a+1
    return a

a = vartest(a)
print(a)

#2) global 명령어 사용 > 추천 안함
a =1 
def vartest():
    global a 
    a = a+1

vartest()
print(a)




