#문자열을 slice한 결과와 id() 및 is() 연산자 출력 결과를 말해보시오.

#[1]: 문자열
t = "korea"

#[2]: 슬라이스 및 id()출력
print(t,id(t),'-',t[:1],id(t[:1]))
print(t[:],id(t[:])) #이것도 슬라이스 한 거지만 아무런 변화가 없기 때문에 메모리 주소가 같게 나온다

#[3]: is 연산자 결과
print('-'*140)
print('t is t[:] =',t is t[:])
print('t is t[:1] =',t is t[:1])
print('t[:1] is t[:2] =',t[:1] is t[:2])
print('t[:] is t[:5] =',t[:] is t[:5])