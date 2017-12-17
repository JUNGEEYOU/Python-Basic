#6. 외장 함수
#1) sys모듈: 1) 명령 행에 인수 전달 
import sys
#sys.exit() #2) 강제 종료 
print(sys.argv)  #변수 
#- 3) 자신이 만든 모듈 불러와 사용하기 sys.path
# print(sys.path)

#2) pickle : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있는 모듈 
# import pickle
# f = open("test.txt",'w')
# data = {1:'python', 2: 'you need '}
# pickle.dump(data, f)
# f.close()


#3) os모듈 : 환경 변수나 디렉터리, 파일 등의 os 자원을 제어
# import os
# print(os.environ)
# print("path: ",os.environ['PATH'])
# print("os.getcwd()",os.getcwd())

#4) calendar
# import calendar
# print(calendar.calendar(2017))
# print(calendar.prmonth(2017,12))


#5) webbrowser
# import webbrowser
# webbrowser.open("http://google.com")





