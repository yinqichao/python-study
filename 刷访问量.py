import requests

url = 'https://app.tmuyun.com/webDetails/news?id=9983778&tenantId=61&uid=6376f3a0010ef612bf4c9a3f'

for i in range(1, 10000):
    result = requests.get(url)
    print(f'{i}---{result.status_code}')
