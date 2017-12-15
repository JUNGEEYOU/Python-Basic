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










