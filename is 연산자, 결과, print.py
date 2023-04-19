#아래 코드의 is 연산자 결과 및 각각의 print 결과를 예상하여 말해보시오.

a = "korea"
print('[1]',a,id(a))

b = "korea"
print('[2]',b,id(b))
print('a is b =',a is b)

b += "!"
print('[3]',b,id(b)) #korea!
print('a is b =',a is b)

c = b[:-1] #[:2]면 2전까지 니까 ko까지 나옴 헷갈리면 2개의 문자가 나온다고 생각하면 됨
print('[4]',c,id(c)) #korea
print('a is c =',a is c) #같은 korea이지만 슬라이스한 건 따로 메모리에 할당을 한다.
