import View

View.view()

id = '1234'
pw = '5678'
button = True
while(button):
    input_id = input("ID : ")
    input_pw = input("PW : ")
    if(input_id == '0'):
        break
    if(input_id == id and input_pw == pw):
        print("Success")
        print(View.EditFile.edit_lotto_num)
        print(View.EditFile.bonus_num)
        break
    else:
        print("Retry!")