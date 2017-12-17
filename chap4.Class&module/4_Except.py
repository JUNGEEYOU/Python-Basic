#4. 예외 처리 
# try: 4/0
# except ZeroDivisionError as e:
#     print(e)


#2) try~else: else는 except절 바로 다음에 위치해야함 
# try: 
#     f = open('foo.txt','r')
# except FileNotFoundError as e:
#     print(str(e))
# else: 
#     data = f.read()
#     f.close()


#3) try~finally 

#4) 오류 회피하기 : pass 넣기 
# try: 
#     f = open('foo.txt','r')
# except FileNotFoundError as e:
#     pass  
# else: 
#     data = f.read()
#     f.close()


#5) 일부러 오류 발생시키기 : raise 
class Bird: 
    def fly(self): 
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print('very fast')

eagle = Eagle()
eagle.fly() 