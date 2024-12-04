import Analyze
import EditFile
import operator

'''
#Main
*Group
 1조 : 52.32% 
 2조
 3조
 4조
 5조
 
 상위 3개 : 
   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
1                                           최다빈도 : 
2
3
4
5
6

 #
'''
def view():
    EditFile.editFile()
    main_DB, bonus_DB = Analyze.analyze()
    total = len(EditFile.bonus_num)
    print('## Main ')
    print('*Group')
    for i in main_DB.group_num.keys():
        print(f'{i}조 : {round((main_DB.group_num[i] / total) * 100, 2)}%')
    print(f'최다 빈도수 : {max(main_DB.group_num, key = main_DB.group_num.get)}  {round((main_DB.group_num[i] / total) * 100, 2)}%')
    
    print('\n   0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')
    
    for i in range(0, 6):
        print(f'{i + 1} : ', end = "")
        for j in range(0, 10):
            print(f'{round((main_DB.num_table[i][j] / total) * 100, 2)} ', end="")
        print(f"최다 빈도 수 : {main_DB.num_table[i].index(max(main_DB.num_table[i]))} - {round((max((main_DB.num_table[i])) / total) * 100, 2)}%")
    
    print('##Bonus')
    print('\n   0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |')
    
    for i in range(0, 6):
        print(f'{i + 1} : ', end = "")
        for j in range(0, 10):
            print(f'{round((bonus_DB.num_table[i][j] / total) * 100, 2)} ', end="")
        print(f"최다 빈도 수 : {bonus_DB.num_table[i].index(max(bonus_DB.num_table[i]))} - {round((max((bonus_DB.num_table[i])) / total) * 100, 2)}%")