#대문자 A,B,C 3개 문자에 대해서 아스키 코드로 출력하는 코드를 작성하시오


#[1]: 대문자 A--> 넌 정체가 뭐냐?
print('A',type('A'))
print(ord('A')) #ord()함수는 문자를 입력받아 해당 문자에 해당하는 아스키 코드 값을 반환 (ordinal number)
print(ord('B'))
print(ord('C'))
print(ord('Z')) #A(65) + 알파벳 문자(26개-1) = Z(90)


#[2]: 소문자 a --> 넌 또 정체가 뭐냐?
print('a',type('a'))
print(ord('a')) #97
print(ord('b'))
print(ord('c'))
print(ord('z')) #a(97) + 알파벳 문자(26개-1) = z(122)