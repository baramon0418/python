Kscore = int(input("국어 점수를 입력해주세요: "))
Escore = int(input("영어 점수를 입력해주세요: "))
Mscore = int(input("수학 점수를 입력해주세요: "))

if (Kscore >= 0 and 100 >= Kscore) and (Escore >= 0 and 100 >= Escore) and (Mscore >= 0 and 100 >= Mscore):
    
    avg = (Kscore + Escore + Mscore) / 3

    if 90 <= avg:
        print("A")

    elif 80 <= avg:
        print("B")

    elif 70 <= avg:
        print("C")

    else:
        print("F")

else:
    print("입력 범위 오류")
