import requests
import json

apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjYwMTk2NjQ3LCJ1aWQiOjE1MDUyOTg5LCJpYWQiOiIyMDIwLTA3LTE2VDEzOjUyOjIxLjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.oreGn_KpT41Ip0EhBBeTB_E1MynLpnPMA0G8jOKVLrE"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization" : apiKey}

query = '{boards (ids: 652383291) { activity_logs { id event data created_at user_id entity account_id  }}}'
data = {'query' : query}

json_formatted_str = json.dumps(data, indent=2)

r = requests.post(url=apiUrl, json=data, headers=headers)

pretty_json = json.loads(r.text)
print(pretty_json)
print(json.dumps(pretty_json ))
print(json.dumps(pretty_json , indent=1))