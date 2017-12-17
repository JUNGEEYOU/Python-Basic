#5. 내장 함수 : import 없이 사용가능 
#1) abs(): 절대값
print('abs(-3):', abs(-3))
#2) all(x):x 모두가 참이면 true, 하나라도 거짓이면 false 
print('all([2,3,4]):', all([2,3,4]))
print('all([2,3,4,0]):', all([2,3,4,0]))

#3) any(x) :x중 하나라도 참이면 true
print('any([2,3,4,0]):', any([2,3,4,0]))
print('any([0]):', any([0]))

#4) chr(x) : 아스키 코드값을 입력으로 받아 문자 출력 
print('chr(97):',chr(97))

#5) dir: 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다
print('dir([1,2,3]):',dir([1,2,3]))

#6) divmod(a,b): 2개의 숫자를 나눈 몫과 나머지를 튜플형태로 리턴함
print("divmod(7,3): ",divmod(7,3))

#7)enumerate: 열거하다라는 뜻으로 리스트 튜플 문자열을 입력으로 받아 인덱스 값을 포함하여 리턴 / 인덱스가 필요할 경우 사용\
for i,name in enumerate(['body','foo','bar']):
    print(i,name)

#8) eval(): 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 리턴
print("eval('1+2'): ",eval('1+2'))

#9) filter(함수, 매개변수) : 함수에서 참인 것만 출력
def positive(numberList):
    result =[]
    for num in numberList:
        if num >0:
            result.append(num)
    return result
print(positive([1,-3,2,0,-5,6]))

def positive(x):
    return x>0

print(list(filter(positive,[1,-3,2,0,-5,6])))


#10) hex 16진수로 변환 
print("hex(234):",hex(234))

#11) id(object) 객체의 주소값을 리턴
a =3 
print('(id(a):',id(a))

#12) input([prompt])
#13) int(x): 정수로 변환 
print("int('3')",int('3'))
print("int('3')",int(3.6))

#14) isinstance(object, class): 참 거짓

#15) lambda: 함수를 생성할 때 예약어 def와 동일한 역할 (but 간편함)
sum = lambda a,b:a+b
print("sum(3,2):",sum(3,2))

#- 
myList = [lambda a,b: a+b, lambda a,b: a*b]
print('myList[0](3,2)',myList[0](3,2))
print('myList[1](3,2)',myList[1](3,2))

#16) len(s): s의 길이 리턴 
print("len('python):",len("python"))

#17) list(s): s를 입력 받아 리스트로 리턴
print("list('python'): ",list("python"))
print("list((1,2,3)): ",list((1,2,3)))

#18) map(f,iterable): 반복 리턴해줌 
def two_times(x): return x*2
print("map(two_times,[1,2,3,4]):",list(map(two_times,[1,2,3,4])))

#19) max 최소값 리턴 /min
print("max([1,2,3]):",max([1,2,3]))
print("max(''python):",max('python'))
print("min([1,2,3]):",min([1,2,3]))
print("min(''python):",min('python'))

#20) ord(c) 문자의 아스키 코드값을 리턴
print("ord('a'):",ord('a'))
#21) pow(x,y)
print("pow(2,4):",pow(2,4))

#22) zip 동일 개수로 이루어진 자료형을 묶어줌 
print("list(zip([1,2,3],[4,5,6]))",list(zip([1,2,3],[4,5,6])))
