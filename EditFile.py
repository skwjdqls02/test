
num_history = []
edit_lotto_num = []
bonus_num = []

def editFile():
    f = open("./LottoDB/LottoNumHistory.txt", 'r', encoding='UTF8')
    num_history = f.readlines()

    f.close()

    for i in range(0, len(num_history)):
        num_history[i] = num_history[i].strip()
    #print(num_history)

    for i in range(0, len(num_history)//4):
        edit_lotto_num.append(num_history[(i * 4) + 2].replace(" ", ""))
        bonus_num.append(num_history[(i * 4) + 3].replace(" ", ""))

editFile()