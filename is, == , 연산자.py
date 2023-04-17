#아래 코드의 is, == 연산자의 결과로 출력되는 값을 예상하여 말해보시오.
#결과는 True, False 값으로 출력된다.

#[1]: 숫자
a = 101
b = 100+1
print('[1-1]a is b',a is b)
print('[1-2]a == b',a == b)
#101이 같은 메모리에 할당되기 때문에 둘 다 true임

#[2]: 문자열
c = 'korea'
d = 'korea'
print('[2-1]c is d',c is d)
print('[2-2]c == d',c == d)
#korea가 같은 메모리에 할당되기 때문에 둘 다 true임

#[3]: 리스트
e = [1,2,3,4,5]
f = [1,2,3,4,5]
print('[3-1]e is f',e is f)
print('[3-2]e == f',e == f)
#리스트는 같은 값을 가지고 있어도 서로 다른 메모리 주소로 할당이 된다.