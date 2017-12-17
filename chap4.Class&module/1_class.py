# 1. 파이썬 프로그래밍의 핵심, 클래스 
# 1) 클래스 변수 
class Service:
    secret ="영구는 배꼽이 두개다"

pey = Service()
print(pey.secret)

#2) 클래스 함수 
class Service:
    secret ="영구는 배꼽이 두개다"
    def sum(self, a,b):  #함수 정의 시 무조건 self 해야함
        result = a+b
        print('%s +%s = %s 입니다' %(a,b,result))

pey = Service()
pey.sum(1,1)

#3) self 알아보기 
class Service:
    secret ="영구는 배꼽이 두개다"
    def setname(self, name):
        self.name =name

    def sum(self, a,b):  #함수 정의 시 무조건 self 해야함
        result = a+b
        print('%s님 %s +%s = %s 입니다' %(self.name,a,b,result))

pey = Service()
pey.setname('정이')
pey.sum(1,1)

#4) __init__이란? 변수 값 초기화 생성자 함수 


#5) 계산기 만들기 
class FourCal: 
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result  
    def mul(self):
        result = self.first * self.second
        return result   
    def div(self):
        result = self.first / self.second
        return result    


a = FourCal()
a.setdata(1,3)
print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())

#6) 유씨네 집 클래스 만들기 
class HousePark:
    lastname ="유"
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print('%s, %s여행을 가다'%(self.fullname, where)) 

pey = HousePark('정이')
pey.travel('태국')


#7) 클래스 상속: class 상속받을 클래스(상속할 클래스):

class HouseKim(HousePark):
    lastname = "김"

pey2 = HouseKim('정이')
pey2.travel('태국')

#8) 메서드 오버라이딩 : 메서드를 다시 구현 하면됨!!!
class HouseKim(HousePark):
    lastname = "류"
    def travel(self, where,day):
        print('%s, %s여행을 가다 %d일 동안'%(self.fullname, where, day)) 


pey2 = HouseKim('정이')
pey2.travel('태국',7)

#9) 연산자 오버로딩  : 연산자를 객체끼리 사용하도록 하는 기법 
class HousePark:
    lastname ="유"
    def __init__(self,name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print('%s, %s여행을 가다'%(self.fullname, where)) 

    def love(self, other):
        print('%s %s 사랑에 빠졌네'%(self.fullname, other.fullname))
    def __add__(self, other):  # +연산자
         print('%s %s 결혼했네'%(self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "류"
    def travel(self, where,day):
        print('%s, %s여행을 가다 %d일 동안'%(self.fullname, where, day)) 

pey = HousePark('정이')
jumg = HouseKim('쩡이')
pey.love(jumg)
pey + jumg