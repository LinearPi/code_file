import random

import pandas as pd
# orid_list = []
# for i in range(30):
#     orid_list.append(random.randint(1,10))
# print(orid_list)

list_finish = [7, 10, 5, 2, 1, 2, 6, 2, 5, 4, 10, 2, 6, 2, 8, 10, 8, 7, 1, 4, 8, 1, 2, 5, 10, 7, 1, 6, 6, 10]


def analysis_data(dataes):
    odd_num = 0    # 奇数
    even_num = 0   # 偶数
    fenmu = 0    # 求概率是用的分母
    odd_time = []   # 奇数的出现个数
    even_time = []  # 偶数的出现个数
     
    odd_list = []   # 奇数出现几次之后偶数出现
    even_list = []  # 偶数出现几次之后奇数出现 
    even_time_num = []  # 
    odd_time_num = []   #


    for data in dataes:
        if data %2 == 0:
            even_num +=1
            even_time.append(odd_num)
        else:
            odd_num +=1 
            odd_time.append(even_num)
    # print(even_time)
    # print(odd_time)

    for ev in set(even_time):
        even_list.append(even_time.count(ev))
    even_list.sort()
    # print(even_list) # 偶数出现的数据
    # print('*'*10)

    for num in set(odd_time):
        odd_list.append(odd_time.count(num)) # 奇数几次之后是偶数的的列表
    # print(odd_list)   # 奇数出现的数据
    
    even_time_num = set(even_list)
    even_sort_time_num = list(even_time_num)
    even_sort_time_num.sort()

    # 开始求概率 贝叶斯理论 在出现N偶数的情况下奇数出现的概率，P(odd|even(N))
    fenmu = len(even_list)
    print(even_list)
    print(even_sort_time_num)
    print(fenmu)
    
    print('*'*10)
    pro_num = []
    show_pro = []
    times = []

    for prob in even_sort_time_num:    
        times.append(even_list.count(prob))      
        pro_num.append((even_list.count(prob))/fenmu)
        show_pro.append(even_list.count(prob)/len(even_list))  
        fenmu -=even_list.count(prob)
            
    for i in range(0,len(pro_num)):
            print('从偶数变成奇数的次数是{}，一共出现了几次{}，概率为{}, \n 出现{}，的概率是{}'
            .format(even_sort_time_num[i],times[i],pro_num[i], even_sort_time_num[i] ,show_pro[i]))

    # print(even_num, odd_num, probability_set, len(odd_list), pro_num)

    


def main():  
    analysis_data(list_finish)


if __name__ == "__main__":
    main()