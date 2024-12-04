import View

View.view()


button = True

while(button):
    print("1. 전체 출력 2. 당첨번호만 출력 3. 보너스만 출력 4. 종료")
    choice = int(input("선택 : "))
    if choice == 1:
        print(View.EditFile.edit_lotto_num)
        print(View.EditFile.bonus_num)
    elif choice == 2:
        print(View.EditFile.edit_lotto_num)
    elif choice == 3:
        print(View.EditFile.bonus_num)
    elif choice == 4:
        print("bye")
        button = False
    else:
        print("try again!")