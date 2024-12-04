import EditFile as file

class analyze_DB:
    main_num = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0} # 조를 제외한 나머지 번호의 출현 빈도
    num_table = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 1번째
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 2번째
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 3번째
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 4번째
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 5번째
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # 6번째 번호(0 ~ 9)
                 ]
    
class add_group_DB(analyze_DB):
    group_num = {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0} # {group_num}조
    
def analyze():
    
    main_DB = add_group_DB()
    for i in range(0, len(file.edit_lotto_num)):
        n = file.edit_lotto_num[i]  # *조******
        main_DB.group_num[n[0]] += 1 # 조 번호 카운트

        for j in range(2, 8): # *조[******]
            main_DB.main_num[n[j]] += 1 # 출현 빈도 카운트
            main_DB.num_table[j - 2][int(n[j])] += 1 # 각번째 번호 빈도 수
    
    bonus_DB = analyze_DB()
    for i in range(0, len(file.bonus_num)):
        n = file.bonus_num[i]
        for j in range(0, 6):
            bonus_DB.main_num[n[j]] += 1
            bonus_DB.num_table[j][int(n[j])] += 1
        
    return main_DB, bonus_DB
