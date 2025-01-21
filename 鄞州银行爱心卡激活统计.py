import json

import pandas as pd
import requests

sn_map = {
    'S6805370016569': 0,
    'S6805370016570': 0,
    'S6805370016571': 0,
    'S6805370016572': 0,
    'S6805370016573': 0,
    'S6805370016574': 0,
    'S6805370016575': 0,
    'S6805370016576': 0,
    'S6805370016577': 0,
    'S6805370016578': 0,
    'S6805370016579': 0,
    'S6805370016580': 0,
    'S6805370016581': 0,
    'S6805370016582': 0,
    'S6805370016583': 0,
    'S6805370016584': 0,
    'S6805370016585': 0,
    'S6805370016586': 0,
    'S6805370016587': 0,
    'S6805370016588': 0,
    'S6805370016589': 0,
    'S6805370016590': 0,
    'S6805370016591': 0,
    'S6805370016592': 0,
    'S6805370016593': 0,
    'S6805370016594': 0,
    'S6805370016595': 0,
    'S6805370016596': 0,
    'S6805370016597': 0,
    'S6805370016598': 0,
}

url = 'https://yl.mzt.zj.gov.cn/zj_jxpj/zjszhyl/lovecard-intact-cms/auth/yllovecard/pagination'

cookie = '_zcy_log_client_uuid=b7f9a860-31d2-11ef-a9f3-832c246d299b; UM_distinctid=190d9a36397580-06c6dea9795797-19525637-13c680-190d9a36398c55; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219241b0a39fbb3-01e184cf9bfce8d-16525637-1296000-19241b0a3a0664%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTkyNDFiMGEzOWZiYjMtMDFlMTg0Y2Y5YmZjZThkLTE2NTI1NjM3LTEyOTYwMDAtMTkyNDFiMGEzYTA2NjQifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219241b0a39fbb3-01e184cf9bfce8d-16525637-1296000-19241b0a3a0664%22%7D; sensorsdata2015jssdksession=%7B%22session_id%22%3A%221932895067c9410c206522c3f35b81f52563612960001932895067d12ff%22%2C%22first_session_time%22%3A1731552675451%2C%22latest_session_time%22%3A1731552695057%7D; user-center-auth-server=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbklkIjozOTc0MjUsInJuIjoiMkwwd2lwRkxJd0lGWERKWWVJWmd2c1FsMmpxZXNZVHciLCJ1c2VySWQiOjM5NzQyNSwidXNlck5hbWUiOiJGODFDM0U0QUY5QkFCQjMxMTEyRUJBRkNGNjRGRjc2MSIsImFyZWFDb2RlIjoiMzMwMjEyIn0.1W5lQZrtmStBFlmUtp8dGF0_3IPui38D3xo4i4bAX-8; wzws_sessionid=gjc1NGRkYaBnhiONgTA4NDViM4AxMTUuMjMxLjIxNC4xMDI=; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImRkOTJjMjIzLWUzNzgtNDU1Yi04MmEyLTAwNWMzNDFmNzVjOSJ9.OPxwTTdPXDNkFgWCl5lXriPF65NRHg3pgCGyeM30B7LKauFipAIdMqn-vEbUB3He20AAr40SnoijVCCThxz8Hg; app-admin-server-token=31f48054-b2b1-4b22-944e-aaafb6b26a63; JSESSIONID=4FD04634122CCE27B615CC508D32A2AB; _uapp_n_70=f96071fe-b67c-4d7d-9966-876a2e8a955a'

headers = {'Cookie': cookie}

data = {
    "sdStatusCard": "03",
    "termType": "02",
    "areaCode": "330212",
    "source": 1,
    "pageNo": 1000,
    "pageSize": 100
}

result = requests.post(url, headers=headers, json=data)

elderly_list = json.loads(result.content.decode('utf-8'))

for item in elderly_list['resultList']:
    if item['termSn'] in sn_map:
        sn_map[item['termSn']] = sn_map[item['termSn']] + 1

print(sn_map)

# Convert the sn_map to a DataFrame
df = pd.DataFrame(list(sn_map.items()), columns=['序列号', '激活人数'])

# Export the DataFrame to an Excel file
df.to_excel('/Users/yinqichao/Downloads/sn_map.xlsx', index=False)
