#2 * i = 2*i

#for i in range(1,10,1) :
#    print("2*"+str(i),"= "+str("%2d"%(i*2)))

#for i in range(1,10,1) :
#    print("3*"+str(i),"= ","%2d"%(i*3))

#for i in range(1,10,1) :
#    print("4*"+str(i),"= ","%2d"%(i*4))

#중첩 for문으로 구구단 만들기
#for i in range(2,10,1) :
#    print(" ") #1단이 나올 때마다 띄어쓰기 
#    for j in range(1,10,1):
#        print(str(j)+"*"+str(i),"= "+str("%-3d"%(i*j)),end=" ")
     

#문제1
#1****
#*1***
#**1**
#***1*
#****1
"""
for i in range(5): #i는 0부터 4까지 5행 
    for j in range(5): #5열
        if i==j:
            print("1", end="")
        else:
            print("*", end="")
        
    print("")





#문제2
#1      1
#12     3
#123    6
#1234   10
#12345  15
h=0
for i in range(1,4,1): #3줄 
    for j in range(1,i+1): #숫자 출력을 위한 for
        h=h+j
        print("%2d"%j,end="")
    for k in range(10,i,-1): #띄어쓰기를 위한 for
        print("  ", end="")
        
    print("%2d"%h,"\n")
    h=0


#i=1 #시작을 전해줘야 함 
#while(i<6):
#    print(i)
#    i=i+1


#무한루프
x=1
while True:
	if x==101: #100번까지 출력
		break
	#print(x,"=김진희")
	x=x+1 #몇번했는지 세고 싶을 때



#3의 배수 출력하고 갯수 출력 
count=0
for i in range(1,101,1):
    if i % 3 == 0:
        print(i,end=" ")
        count = count+1
print("\n갯수: ",count)
        



#임의의 수를 계속 입력받아 합을 구하는 코딩이다
#숫자 0이 들어오면 입력을 멈추고 합을 출력한다
hap = 0
while True:
    num = int(input("숫자를 입력해주세요: "))
    if num == 0:
        break
    hap = hap + num
print("합:",hap)


num = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    num[i]=int(input("숫자"))
print(num)
num.append(100)




num1 = [0,0,0,0]
for i in range(4):
    num1[i]=int(input("숫자"))
    hap = hap+num1[i]
print(num)


numList = []
numList.append(0)
numList.append(0)
numList.append(0)
numList.append(0)
print(numList)


num=[]
for i in range(4):
    num[i] = 0
    num.append(0)
"""
#리스트를 하나 만들어서 숫자 데이터 5개 저장한다
#리스트의 데이터 중에서 5보다 큰 데이터가 몇개인지 세어서 출력
#리스트의 데이터를 정렬시켜서 출력한다
"""
list = [0,0,0,0,0]
for i in range(5):
    list[i] = int(input("리스트에 숫자 입력:"))
sort(list)
if list[i] > 5:
    list.count
"""
listlen=0
count1=0
Mylist = [36,12,2,6,3]
for i in range(5): #5보다 큰 데이터 갯
    Mylist.sort()
    if Mylist[i] > 5:
        count1+=1
print("갯수:",count1)
Mylist.sort()
print(Mylist) #정렬

for j in range(4,-1,-1): #5보다 큰 데이터 삭제 
    Mylist.sort()
    if Mylist[j] > 5:
        del(Mylist[j])
print(Mylist)    


