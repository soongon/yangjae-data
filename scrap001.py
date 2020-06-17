import requests
from bs4 import BeautifulSoup

# HTML 확보
res = requests.get('https://www.naver.com/')

# HTML 파싱을 위한 bs4 준비
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)

# 내가 원하는 데이터를 추출..
the_tag = soup.select_one('#themecast > div.theme_cont > div:nth-child(2) > div > ul > li:nth-child(2) > a.theme_info > strong')
print(the_tag)


