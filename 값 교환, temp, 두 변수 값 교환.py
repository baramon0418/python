#a,b 각각의 변수에 들어있는 값을 교환하는 코드를 구현하시오.
#a,b 변수에 들어있는 값은 100,200이다.

#[1]:변수 선언 및 값 할당
a = 100
b = 200
print('[1] 교환 전 a,b 변수의 값은 =',a,b)

#[2]:변수 swap
# a = b
# b = a
# print('[2] 교환 후 a,b 변수의 값은 =',a,b) #200 200

#[2]: temp 변수를 이용한 swap
# temp = a #100
# a = b #200
# b = temp
# print('[2] 교환 후 a,b 변수의 값은 =',a,b)

#[3]: temp 변수를 이용하지 않고 swap
a,b = b,a
print('[3] 교환 후 a,b 변수의 값은 =',a,b)
