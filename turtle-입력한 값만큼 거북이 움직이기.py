import turtle

turtle.shape('turtle')
turtle.pensize(5) #펜의 두께: 5
turtle.pencolor("blue") #펜의 색상: 파란색

while True :
    angle = int(input("거북이의 회전 각도 : "))
    distance = int(input("거북이가 이동 거리 : "))    

    turtle.right(angle)
    turtle.forward(distance)

#for x in range(5): 5번 반복시키기
