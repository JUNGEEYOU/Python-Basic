#2. 문자열 
 #1)  \'로 따옴표 넣기 (이스케이프 코드)
food = 'Python\'s favorite food is perl'  
say = "\"Python is very easy.\" he says"

print("food: ",food)
print("say: ", say)

 #2)  \n 으로 띄어쓰기 
multiline = "Life is too short \n you need python" 
print("multiline: ",multiline)


 #3) 띄어쓰기: """ 사용 or '''사용  
multiline2 = """Life is too short
 you need python"""

print("multiline2: ",multiline2)


#4) 문자열 연산하기 
# - 문자열 더하기 & 곱셈 
head = "python"
tail = ' is fun!'
print('head + tail: ', head + tail)
print('head* 3: ', head*3)

#5) 문자열 인덱싱과 슬라이싱 : 가리킨다, 잘라낸다 
a = 'Life is too short. you need python'
print("a[3]: ", a[3])
print("a[-1]: ",a[-1])
#슬라이싱 [시작: 끝]> 끝은 포함되지 않음!!!!
print('a[0:3]: ',a[0:3]) 
print('a[5:7]', a[5:7])
print('a[19:]',a[19:])  #시작 19부터 끝까지
print('a[:17]', a[:17]) # 0부터 17까지 
print('a[19:-7]: ',a[19:-7] )
#슬라이싱으로 문자열 나누기 
a = '20010331rainy'
data = a[:8]
weather = a[8:]
print('data: ', data)
print('weather: ', weather)
#문자열 바꾸기 
a = 'pithon'
b = a[:1] + 'y' + a[2:]
print('b: ', b)


#6) 문자열 포매팅 : 문자열 내 어떤 값을 삽입하는 방법 
a = "i eat %d apples." %3
print('a: ', a)
b = "i eat %s apples." %'five'
print('b: ', b)
number =4
c = "i eat %d apples." %number
print('c: ', c)
number = 10
day = 'three'
d = 'i ate %d apples. so i was sick for %s days.' %(number, day)
print('d: ', d)
e = 'i have %s apples' %3  #문자열 %s는 어떤 형태의 값이든 변환하여 넣을 수 있음!
print('e: ', e)
f = 'error is %d%% ' %98  # %쓰려면 %%로!!
print('f: ', f)
#- 포맷 코드와 숫자 함께 사용하기 
# - 정렬과 공백 
a = '%10s' %'hi'  # 전체 10을 두고 오른쪽 정렬
print('a: ', a)
b = '%-10sjane.'%'hi'  #%-10s은 왼쪽 정렬
print('b:', b)
c = '%0.4f' %3.2134333
print('c: ', c)
d = '%10.4f' %3.42134234
print('d: ', d)


#7) 문자열 관련 함수들 
# - 문자 개수 세기(count)
a= 'hobby'
print('a.count: ',a.count('b'))
# - 위치 알려주기1(find)
b = 'python is best choice'
print("b.find('b')", b.find('b'))
print("b.find('k')", b.find('k'))  #존재하지 않는 경우  -1
# -위치 알려주기2 (index)
a = 'Life is too short'
print("a.index('t'): ", a.index('t'))
#print("a.index('k'): ", a.index('k'))  #오류 발생!!

#-문자열 삽입 (join)
a= ','
print("a.join('abcd')", a.join('abcd'))  # a의 값인 , 을 문자열의 각각 문자 사이에 삽입 
#-소문자를 대문자로 (upper) / 대문자를 소문자로 바꾸기 (lower)
a = 'hi'
print("a.upper(): ", a.upper())
b = 'HI'
print("b.lower(): ", b.lower())
#- 왼쪽 공백 지우기 (lstrip) / 오른쪽 공백 지우기(rstrip) / 양쪽 공백 지우기 (strip)
a = ' hi'
print("a.lstrip():", a.lstrip())
b = 'hi '
print("b.rstrip():",b.rstrip())
c = ' hi '
print("c.strip():",c.strip())

#- 문자열 바꾸기(replace)
a = "Life is too short"
print("a.replace('Life', 'your leg')", a.replace('Life', 'your leg'))

#- 문자열 나누기(split)
a = 'Life is too short'
print("a.split()", a.split())  # 공백 기준으로 문자열 나눔 
b = "a:b:c:d"
print("b.split(':')", b.split(':'))   # : 기준으로 문자열 나누기 

# - 고급 문자열 포매팅 
a = " i eat {0} apples".format(3)
print('a: ',a )
b = 'i eat {0} apples'.format('five')
print('b: ',b )

number =10 
day ='three'
c = "l ate {0} apples. so i was sick for {1} days.".format(number, day)
print('c: ', c)























