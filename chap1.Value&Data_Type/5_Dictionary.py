#5. 딕셔너리 자료형 : 연관 배열 or 해시 / key~value
dic = {'name':'pay', 'phone':'01029131111', 'birth: ':'0517'}
print('dic', dic)
dic2 = {1: 'hi'}
dic3 = {'a': [1,2,3]}
#-딕셔너리 쌍 추가하기 
dic4 = {1:'a'}
dic4[2] = 'b'
print('dic4', dic4)
dic4['name'] = 'lena'
print('dic4', dic4)
dic4[3] = [1,2,3]
print('dic4', dic4)

#-딕셔너리 요소 삭제하기 
del dic4[1]
print('dic4', dic4)

# 딕셔너리에 접근하기 
print("dic4[2]: ",dic4[2])
print("dic4['name']: ",dic4['name'])

# 주의 사항 : 1)키는 고유하게 설정 중복되면 1개 무시됨! 2)key는 리스트로 쓰면 안됨!!
a= {1: 'a', 1: 'b'}
print('a: ',a)

#2) 딕셔너리 관련 함수들 
#- key리스트 만들기 (keys)
dic = {'name':'pay', 'phone':'01029131111', 'birth':'0517'}
print('dic.keys(): ', dic.keys())
print('list(dic.keys()): ', list(dic.keys()))  #키를 리스트로 변환 

#-value리스트 만들기 (values)
print('dic.values(): ', dic.values())

#-key, value 쌍얻기 (items)
print('dic.items(): ',dic.items())

#-key:value 쌍 모두 지우기 (clear)
dic.clear()
print('dic: ',dic)

#- key로 value얻기 (get)
a ={'name':'pay', 'phone':'01029131111', 'birth':'0517'}
print("a.get('name'): ",a.get('name'))
print("a.get('none'): ",a.get('none'))  #a['none']은 에러를 이 함수는 None 을 리턴
print("a.get('name2','no name'): ",a.get('name2','no name'))  # 디폴트 설정할 수 있음 없으면 출력함 

#- 해당 key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pay', 'phone':'01029131111', 'birth':'0517'}
print("'name' in a:",'name' in a)   #true
print("'email' in a:",'email' in a)   #false

