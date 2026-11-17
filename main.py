while True:
    print("================================")
    print("       Python 퀴즈 게임")
    print("================================")
    print("1. 퀴즈 풀기")
    print("2. 문제 추가")
    print("3. 문제 목록")
    print("4. 최고 점수")
    print("5. 종료")

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
        print("퀴즈를 시작합니다!")
    elif choice == "2":
        print("문제 추가 메뉴입니다.")
    elif choice == "3":
        print("문제 목록 메뉴입니다.")
    elif choice == "4":
        print("최고 점수 메뉴입니다.")
    elif choice == "5":
        print("게임을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다.")

    print()