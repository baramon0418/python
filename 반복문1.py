#print("난생처음 파이썬은 재미있습니다. ^^")
#print("난생처음 파이썬은 재미있습니다. ^^")
#print("난생처음 파이썬은 재미있습니다. ^^")


#for i in range(1,11,1):
#    print("난생처음 파이썬은 재미있습니다. ^^",end=" ")
#    print("i=%d"%i)


#문제1 1부터 10까지 짝수의 합
#sum1 = 0
#sum2 = 0
#for i in range(0,11,2):
#    sum=sum+i
#print("합은:",sum)


#for i in range(1,10,1):
#    if i%2==0:
#        sum1=sum1+i
#    if i%2 !=0:
#        sum2=sum2+i
        
#print("합은:",sum1)
#print("합은:",sum2)



#문제2 2부터 100까지 홀수의 갯수
result = 0
counter = 0
for i in range(2,101,1):
    if i%2 != 0:
        print("%3d"%i, end=" ") #뒤에 스페이스하려면 -3d
        result = result+1
        
print("홀수의 갯수:",result)


#10개씩 줄 나누기
result = 0
counter = 0
for i in range(2,101,1):
    if i%2 != 0:
        if counter % 10 == 0:
            print("") #이거 넣으면 줄바꾸기가 됨 
        else:
            print("%3d"%i, end=" ")
        counter = counter+1
        result = result+1
        
print("\n홀수의 갯수:",result)

