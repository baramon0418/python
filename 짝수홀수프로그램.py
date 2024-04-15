num = int(input("숫자를 입력:"))

if num % 5 == 0:
    if num % 2 == 0:
        print("2와 5의 배수입니다.")
    else:
        print("5의 배수입니다.")
else:
    print("5의 배수가 아닙니다.")
