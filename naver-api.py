import requests
import pandas as pd

params = {
    'query': '코로나19'
}
headers = {
    'X-Naver-Client-Id': 'D27XOJWmhRiNEgPtei5H',
    'X-Naver-Client-Secret': 'Dis2xjQawO'
}
res = requests.get('https://openapi.naver.com/v1/search/blog.json',
                   params=params, headers=headers)
result = res.json()

print(type(result))

result_lists = []

for item in result['items']:
    result_lists.append(
        [item['title'], item['link'], item['description'], item['postdate']])

df = pd.DataFrame(result_lists, columns=['타이틀','링크','설명','날짜'])
df.to_csv('corona_result.csv')
print('mission completed')
