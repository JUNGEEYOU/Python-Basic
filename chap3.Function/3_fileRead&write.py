# 3. 파일 읽고 쓰기 

#1) 파일 쓰기 

# f = open('새파일.txt','w')
# for i in range(1,11):
#     data = '%d 번째 줄입니다 \n' %i
#     f.write(data)
# f.close()

#2) 프로그램 외부 저장된 파일 읽는 방법 
#1) readlin()함수 이용 
# f = open('새파일.txt','r')

# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

#2) readlins()함수 이용 : 모든 라인을 읽어서  각 줄을 리스트로 리턴 
# f = open('새파일.txt','r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

#3) read()함수 이용하기 : 파일 전체 내용 문자열로 리턴 
# f = open('새파일.txt','r')
# data = f.read()
# print(data)
# f.close()


#3) 파일에 새로운 내용 추가하기  : w는 원래 값 다 사라지고 쓰는 것 / a는 원래 내용 유지하고 쓰는것
f = open('새파일.txt','a')
for i in range(11,20):
     data = '%d 번째 줄입니다. \n' %i
     f.write(data)
f.close()

#4) with문과 함께 사용하기 : f를 자동으로 close()
# with open('새파일.txt','w') as f:
#     f.write('life is too short')


#5) sys 모듈로 입력 인수 주기 
import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=" ")