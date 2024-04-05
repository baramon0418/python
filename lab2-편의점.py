coffee = 1800
trikimbap = 1400
bana = 1800
dosi = 4000
coke = 1500
sae = 2000

coffee_su = int(input("캔커피 개수:"))
trikimbap_su = int(input("삼각김밥 개수:"))
bana_su = int(input("바나나우유 개수:"))
dosi_su = int(input("도시락 개수:"))
coke_su = int(input("콜라 개수:"))
sae_su = int(input("과자 개수:"))

total = 0
total = (coffee*coffee_su) + (trikimbap*trikimbap_su) + (bana*bana_su) + (dosi*dosi_su) + (coke*coke_su) + (sae*sae_su)

print("오늘 총 매출액은 ", total, "원입니다")


#total = can * can_su
#total = total + (trikimbap*trikimbap_su)
#total += bana*bana_su
#이렇게 해도 됨

#total = total - 900*10
#total = total - 3500*5

#total = total + 1800*2
#total = total + 4000*4
#total = total + 1500*1
#total = total + 2000*4
#total = total + 1800*5

