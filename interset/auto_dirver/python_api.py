import sensorsanalytics
import time


import requests

url = "https://xiguacity.cloud.sensorsdata.cn/api/auth/login"

querystring = {"project":"正式项目"}

payload = "{\"username\":\"lijie@xigua.city\",\"password\":\"DPt5Az\"}"
headers = {
    'accept': "*/*",
    'content-type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)

# service_name = 'http://sensor.xiguacity.cn:8106/sa?project=production'
# project_token = 'saf212cb00'
# # 从神策分析配置页面中获取数据接收的 URL
# SA_SERVER_URL = 'http://{$http://sensor.xiguacity.cn:8106/sa?project=production}.datasink.sensorsdata.cn/sa?project={$正式项目}&token={$saf212cb00}'

# # 初始化一个 Consumer，用于数据发送
# # DefaultConsumer 是同步发送数据，因此不要在任何线上的服务中使用此 Consumer
# consumer = sensorsanalytics.DefaultConsumer(SA_SERVER_URL)
# # 使用 Consumer 来构造 SensorsAnalytics 对象
# sa = sensorsanalytics.SensorsAnalytics(consumer)

# # 记录用户登录事件
# distinct_id = '7a2406883dd049c5afc7319304c789b9'

# sa.track(distinct_id, 'UserLogin', is_login_id=True)

# sa.close()


# http://sensor.xiguacity.cn:8107/search-users/users/sequence/?project=production#
# distinct_id=6413a59eb4ce4680bac4797f2f5d4566&
# user_id=-2386266040691478469
# &measures%5B0%5D%5Baggregator%5D=count&measures%5B0%5D%5Bfield%5D=&filter%5Bconditions%5D%5B0%5D%5Bfield%5D=user.%24id&filter%5Bconditions%5D%5B0%5D%5Bfunction%5D=equal&filter%5Bconditions%5D%5B0%5D%5Bparams%5D%5B%5D=6413a59eb4ce4680bac4797f2f5d4566&all_page=false&page=0
# 6413a59eb4ce4680bac4797f2f5d4566