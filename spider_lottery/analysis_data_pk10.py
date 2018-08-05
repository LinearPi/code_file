import pandas as pd


def read_data(file_path, columns):
    pk10_data = pd.read_csv(file_path) 
    # print(type(pk10_data))
    print(pk10_data.columns)
    pk10_one_data = pk10_data[::-1][columns]
    pk10_data._info_axis_name
    # print(pk10_one_data)
    return pk10_one_data

def analysis_data(dataes):
    odd_num = 0    # 奇数
    even_num = 0   # 偶数
    # fenmu = 0    # 求概率是用的分母
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
    even_fenmu = len(even_list)
    # print(even_list)
    print(even_sort_time_num)
    print(even_fenmu)
    

    even_pro_num = []
    even_show_pro = []

    for prob in even_sort_time_num:          
        even_pro_num.append((even_list.count(prob))/even_fenmu)
        even_show_pro.append(even_list.count(prob)/len(even_list))  
        even_fenmu -=even_list.count(prob)
            
    for i in range(0,len(even_pro_num)):
            print('偶数连续出现{}次后变成奇数的概率为{}, \n出现偶数{}的概率是{}'.format(even_sort_time_num[i],even_pro_num[i], 
            even_sort_time_num[i] ,even_show_pro[i]))
        # 对于偶数的求解
    
    
    print('*'*10)


    # 对奇数做同样的求概率
    print('*'*10)
    
    odd_time_num = set(odd_list)
    odd_sort_time_num = list(odd_time_num)
    odd_sort_time_num.sort()
    odd_fenmu = len(odd_list)
    # print(odd_list)
    print(odd_sort_time_num)
    print(odd_fenmu)
    
    odd_pro_num = []
    odd_show_pro = []

    for prob in odd_sort_time_num:          
        odd_pro_num.append((odd_list.count(prob))/odd_fenmu)
        odd_show_pro.append(odd_list.count(prob)/len(odd_list))  
        odd_fenmu -=odd_list.count(prob)
            
    for i in range(0,len(even_pro_num)):
            print('奇数连续出现{}次后变成偶数的概率为{}, \n出现奇数{}的概率是{}'.format(even_sort_time_num[i],even_pro_num[i], 
            even_sort_time_num[i] ,even_show_pro[i]))


def main():
    file_path = '/Users/pizi/Documents/git_flie/code_file/pk10.csv'
    dataes = read_data(file_path, 'two')
    analysis_data(dataes)


if __name__ == "__main__":
    main()
    