import random

myhand = input("가위/바위/보 중 하나를 입력하세요: ")

computer = random.choice(["가위","바위","보"])
print("컴퓨터: ", computer)

if myhand == "가위":
    if computer == "가위":
        print("비겼습니다.")
    elif computer == "바위":
        print("컴퓨터가 이겼습니다.")
    elif computer == "보":
        print("내가 이겼습니다.")

elif myhand == "바위":
    if computer == "바위":
        print("비겼습니다.")
    elif computer == "보":
        print("컴퓨터가 이겼습니다.")
    elif computer == "가위":
        print("내가 이겼습니다.")

elif myhand == "보":
    if computer == "보":
        print("비겼습니다.")
    elif computer == "가위":
        print("컴퓨터가 이겼습니다.")
    elif computer == "바위":
        print("내가 이겼습니다.")

else:
    print("가위/바위/보 중 하나를 내세요.")
