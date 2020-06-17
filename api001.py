import requests
import pprint

res = requests.get('https://api.github.com/users/mojombo')
res_json = res.json()

# print(res_json['avatar_url'])

pprint.pprint(res_json)