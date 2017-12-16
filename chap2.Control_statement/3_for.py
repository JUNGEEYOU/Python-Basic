# 3. for 문 
# 1) 전형적인 for문 
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#2) 다양한 for문 사용 
a= [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)

# for 문의 응용 
marks =[90, 25,67,45,80]
number =0
for mark in marks:
    number = number+1
    if mark >=60: 
        print('%d 학생은 합격입니다.'%number)
    else:
        print('%d번 학생은 불합격입니다.' %number)


#for문과 continue
marks =[90, 25,67,45,80]
number =0
for mark in marks:
    number = number+1
    if mark < 60: continue
    print('%d학생 축하합니다. 합격!' %number)

#for문과 함께 자주 사용하는 range함수 
a = range(10)
print('a: ',a)
a = range(1,11)
print('a: ',a)  # 끝 숫자인 11은 포함되지 않음!1~10까지

sum = 0
for i in range(1,11):  #1~10까지 
    sum = sum +i
print('sum: ', sum)


#합격에 range추가 
marks =[90, 25,67,45,80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print('%d학생 축하합니다. 합격!' %(number+1))

#구구단 
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end =" ")  #end 넣은 이유는 다음 줄로 넘어가지 않도록 하기 위해 
    print('')


#리스트 안에 for문 포함하기 
a = [1,2,3,4]
result =[]
for num in a:
    result.append(num*3)
print(result)

#- 간단하게 리스트 내포
result = [num*3 for num in a]
print(result)

#- 리스트 내포 -if문
result = [num*3 for num in a if num%2==0]
print(result)

#- 이중 for 
result = [x*y for x in range(2,10)
                for y in range(1,10)]
print(result)