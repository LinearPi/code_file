from selenium import webdriver



def login_shence():
    # 打开网页
    driver = webdriver.Chrome('/Users/gouweiqi/Documents/code_py/code_file/interset/auto_dirver/chromedriver') 
    driver.get('https://www.xiguacity.cn/admin/students')
    driver.add_cookie({'name' : 'xigua', 
    'path': '/admin/students',
    'value':'sajssdk_2015_cross_new_user=1; Hm_lvt_fceed5f141b12513f2eb067d19fc0c4c=1543631084; did=5b8360adc8d46d4213bc9221; current_cid_r=5bca9af4c8d46d154e82e32a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%225b8360adc8d46d4213bc9221%22%2C%22%24device_id%22%3A%2216767950bde2c3-065c698181575-35627400-1296000-16767950bdf445%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216767950bde2c3-065c698181575-35627400-1296000-16767950bdf445%22%7D; Hm_lpvt_fceed5f141b12513f2eb067d19fc0c4c=1543664993; scratch_time=-1; learning_time=1; _readio_production_session=Z21Oeit5MnZodVZQelBhMUQ5VFVCeUt3UTl4Vk9yNWZVdnkzeGFsdXhKQm84QUtRZlF1dmxpTjhuOStOVzl4UHVUV0VWVWNROVpVRUtpMDR5MWRlblQ1SDlsV3UxVTcvbVk2QTcxcUk4UXQvWmIyblo0cDJoNGZPSEJ5djJJeTVJZWloRkRaby95MkkwUkR3TUx5WG5LUzlqMlJUVTRDTmYvM0JHcFczMENKM29tdEJ3a2FUeVpnQ1JPamhObXg3WXFIOHNVeGhseG1wUHB6QzlvR2JwTlJNaGFDZEZKeUovejM2a09PVE1SUE1ZS2I2L0Z6NFJGV3NrR0huYUdIaE9scit5UmMybXhMdlFkSngwMDdwRXhQQjNzSnhNUTdkN1ZlUnBpb0E4QUVqTHErQ3FKTjhQVDEzeldlY09FeW5oTjdjQjhJM0Z4ZjZHcytmVFEwREFFblQ4V1FNM25EZU9Zb1hkdE9UZWNxeVRZQU8yNDNubFc3OTJuT0swM2txUFJaWDU2UUtkSnBGNllMVmR0NGxJNWVIRjh2NnE4bzNNS2d2S0JUUXR3WFFsZVFScFVCNW9vVUkvbG9XZEk2TXMycnJmWXlTbmdwTFYyaDlHMlRTaVVTdkdJc0VYTzZxTEhSV29Hc3huVk1jdG02WkNycGdxVEFYdXlHSE5lcHdnRE5vbmxTamMveXp4QTBVMzduVEtHYXJZcWRxRi9XNGpxUnljekQ0SU1kS0ozQXpwWEpYbzFpY1hBOWwxelZCSnJtZ1Q5SFRrSE5DNDBwbmtRZWFzMktxWlRPOVRWa1ZlY3hsR1VyWjJoRElBTkM1OVRsT2xiWktQNTQrM2JuMzAvZitSc3dRdS93czNlSTdRSHl2ZGVvRmJFcUtQaXd6UFFkYkhDQk80K1k9LS10QnZPTnFtUWhzZ0gwRmdxZzRFazhBPT0%3D--66dd680c24da3c3108e7346f13dc384923d71557'})
    

    print(driver.title)

if __name__ == "__main__":
    login_shence()