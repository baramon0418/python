i=0
factorial=1 #곱하기라서 0 넣으면 결과가 다 0임
student_num= int(input("학생의 수를 입력해주세요:"))

for i in range(1, student_num+1, 1):
    if(student_num==i):
        print(i,"=",end="")
    else:
        print(i,"*",end="")
        
    factorial = factorial * i #팩토리얼
print(factorial)    
print("입력받은 학생의 수를 순서대로 세우는 경우의 수:", factorial)


#5*4*3*2*1 만들기 


for j in range(5):
    student_num= int(input("학생의 수를 입력해주세요:"))
    fac=1
    for i in range(student_num,0, -1):
        if(1==i): #숫자가 점점 작아져서 1이 마지막 숫자임 
            print(i,"=",end="")
        else:
            print(i,"*",end="")
            
        fac = fac * i #팩토리얼
    print(fac)    
#print("입력받은 학생의 수를 순서대로 세우는 경우의 수:", fac)
