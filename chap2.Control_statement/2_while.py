#2. while 문 
treeHit = 0
while treeHit< 10: 
    treeHit = treeHit +1
    print('나무를 %d 번 찍었습니다. ' %treeHit)

    if(treeHit==10):
        print('나무가 넘어갑니다')

prompt ="""
    1.add
    2.del
    3.list
    4.quit

    Enter number:"""

number =0
while number !=4:
    print(prompt)
    number = int(input())



# break 
# coffee =10 
# money =300
# while money:
#     print('돈을 받았으니 커피를 줍니다.')
#     coffee = coffee -1
#     print('남은 커피 양은 %d' %coffee)
#     if not coffee: 
#         print('커피가 떨어졌습니다. 판매 중지')
#         break

# coffee = 10
# while True:
#     money = int(input('돈을 넣어주세요: '))
#     if money ==300:
#         print('커피를 줍니다.')
#         coffee = coffee-1
#     elif money >300:
#         print('거스름돈 %d주고 커피 줍니다.' %(money-300))
#         coffee = coffee -1
#     else:
#         print('커피를 주지 않습니다')
#         print('남은 커피의 양은 %d 입니다.' %coffee)
#     if not coffee:
#         print('커피가 다 떨어졌습니다.')
#         break


#조건과 맞지 않는 경우 맨 처음으로 돌아가기 (continue)
a =0 
while a<10:     
    a =a+1
    if a%2 ==0: continue
    print(a)

#무한 루프 : ctrl +c 누름 