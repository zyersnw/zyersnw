import random


def computer_choice():
    choices = ["가위", "바위", "보"]
    return random.choice(choices)


player_score = 0
computer_score = 0
draw = 0
while True:

    while True:
        computer_selection = computer_choice()
        player_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
        if player_choice == "가위":
            print(f"사용자 : {player_choice}!, 컴퓨터 : {computer_selection}!")
            break
        elif player_choice == "바위":
            print(f"사용자 : {player_choice}!, 컴퓨터 : {computer_selection}!")
            break
        elif player_choice == "보":
            print(f"사용자 : {player_choice}!, 컴퓨터 : {computer_selection}!")
            break
        else:
            print("유효한 입력이 아닙니다.\n")
    while True:
        if player_choice == "가위" and computer_selection == "가위":
            print("무승부!!\n")
            draw += 1
            break
        elif player_choice == "가위" and computer_selection == "바위":
            print("컴퓨터 승리!!\n")
            computer_score += 1
            break
        elif player_choice == "가위" and computer_selection == "보":
            print("사용자 승리!!\n")
            player_score += 1
            break
        elif player_choice == "바위" and computer_selection == "가위":
            print("사용자 승리!!\n")
            player_score += 1
            break
        elif player_choice == "바위" and computer_selection == "바위":
            print("무승부!!\n")
            draw += 1
            break
        elif player_choice == "바위" and computer_selection == "보":
            print("컴퓨터 승리!!\n")
            computer_score += 1
            break
        elif player_choice == "보" and computer_selection == "가위":
            print("컴퓨터 승리!!\n")
            computer_score += 1
            break
        elif player_choice == "보" and computer_selection == "바위":
            print("사용자 승리!!\n")
            player_score += 1
            break
        else:
            print("무승부!!\n")
            draw += 1
            break
    re = input("다시 하시겠습니까? (y/n): ")
    if re == "n":
        print(
            f"게임을 종료합니다.\n전적 : 승 {player_score}, 패 {computer_score}, 무 {draw} \n")
        break
