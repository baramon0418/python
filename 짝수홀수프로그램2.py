num = int(input("숫자를 입력:"))

if num % 5 == 0:
    if num % 2 == 0:
        print("2와 5의 배수입니다.")
    else:
        print("5의 배수입니다.")
else:
    print("5의 배수가 아닙니다.")

if num % 5 == 0 and num % 2 == 0:
        print("2와 5의 배수입니다.")

elif num % 5 == 0:
    print("5의 배수")

elif num % 2 == 0:
    print("2의 배수")

else:
    print("2와 5의 배수가 아니다")
