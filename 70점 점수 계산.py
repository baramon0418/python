jum1 = float(input("필기 성적: "))
jum2 = float(input("실기 성적: "))

avg = (jum1 + jum2) / 2

if avg >= 70:
    print("평균 점수: ","%.2f"%avg ,"합격입니다")

else:
    print("평균 점수: ","%.2f"%avg,"불합격입니다")
    
#출력 결과를 소수 2자리까지

if avg >= 90:
    print("A")

elif avg >= 80:
    print("B")

elif avg >= 70:
    print("C")

