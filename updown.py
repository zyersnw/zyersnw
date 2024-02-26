import random

best_try = float('inf')
while True:
    print("\n컴퓨터와 업다운 게임 시작합니다.\n")
    random_number = random.randint(1, 100)
    print("1~100 숫자 하나 입력해주십시오.")
    count = 0
    while True:
        input_number = input()
        try:
            p_number = int(input_number)
            if random_number == p_number:
                count += 1
                print("정답 입니다.\n")
                print(f"시도한 횟수는 {count}번 입니다.\n")
                if count < best_try:
                    best_try = count
                break
            elif random_number > p_number and p_number > 0:
                count += 1
                print("당신이 고른 번호보다 UP!!")
            elif random_number < p_number and p_number < 100:
                count += 1
                print("당신이 고른 번호보다 DOWN!!")
            else:
                print("'''1~100'''사이 숫자를 입력해주십시오.\n")
        except ValueError:
            print("1~100사이 '''숫자'''를 입력해주십시오.\n")

    print(f"고생하셨습니다. 역대 가장 빠르게 정답을 맞춘 시도는 {best_try}번입니다. \n")
    out = input("새롭게 다시하시려면 아무거나 입력, 종료하시려면 out 을 입력해주세요.\n")
    if out == "out":
        break
