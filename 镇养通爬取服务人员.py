import json

import requests

list_url = 'http://218.0.7.136:17002/spb/openapi/V1/attendant/list?keywords=&workState=1&healthCertStatus=&pageIndex=1&pageSize=100'

detail_url = 'http://218.0.7.136:17002/spb/openapi/V1/attendant/detail?id='

authorization = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3NmIyODczNC1mMGMwLTQ2NjUtYWViYi1mYjAyNWUyNmU0MmYiLCJVc2VySWQiOiIyOCIsIlVzZXJOYW1lIjoi5bGF5a625LmQ5YGl5bq3IiwiU2VydmljZU9yZ2FuaXphdGlvbklkIjoiMjgiLCJTZXJ2aWNlT3JnYW5pemF0aW9uR3VpZCI6IjM4ZWZiMjc0ZjU3YzQzMjY5NzNkNjNjMzgwNDM0MGZiIiwiU3RyZWV0SWRzIjoiNyIsIkNvbW11bml0eUlkcyI6IjI3LDI4LDI5LDMwLDMxLDMyLDMzLDM0LDM1LDM2LDEyMywxMjQsMTMwIiwiU2VydmljZVR5cGUiOiIxLDIsMyw0LDUiLCJTZXJ2aWNlSXRlbSI6IjQsNSw2LDcsNzcsNzgsNzksODAsODEsODIsODMsODQsODUsODYsODcsODgsODksOTAsOTEsOTIsOTMsOTQsMTAsMTEsMTIsMTMsMTQsMTUsMTYsMTcsMTgsMTksMjAsOTUsOTYsOTciLCJTZXJ2aWNlTmF0dXJlIjoiMyIsIlN3aXRjaEFjY291bnQiOiJGYWxzZSIsIkp1bXBVc2VyIjoid2JVRDc1N1V5Um89IiwibmJmIjoxNzI5ODM1MjU5LCJleHAiOjE3Mjk5MjE2NTksImlzcyI6ImxleGlhbmdfMjAyMzAyMTUiLCJhdWQiOiJsZXhpYW5nXzIwMjMwMjE1In0.IsGt2Sv6JhM3qHi2_V4om2Q6CH5e3GWNBVf0YsIpFsI'

result = requests.get(list_url, headers={'Authorization': authorization})

huliyuan_list = json.loads(result.content.decode('utf-8'))

final_list = []

for item in huliyuan_list['data']['rows']:
    result = requests.get(detail_url + str(item['id']), headers={'Authorization': authorization})
    huliyuan_detail = json.loads(result.content.decode('utf-8'))

    item["idCard"] = huliyuan_detail['data']['idCard']

    final_list.append(item)

print(final_list)
print(len(final_list))
