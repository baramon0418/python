#1파운드 = 0.453592kg
#1kg = 2.204623파운드 
pound = int(input("파운드(lb)를 입력하세요:"))
kg = pound * 0.453592
print(pound, "파운드(lb)는", round(kg,2) ,"킬로그램(kg)입니다")

kg = int(input("킬로그램(kg)을 입력하세요:"))
pound = kg * 2.204623
print( kg, "킬로그램(kg)은", "%.2f"%pound ," 파운드(lb)입니다")
#%.2f%는 소수점 2번째짜리까지 출력
#%d를 하면 정수 형태
