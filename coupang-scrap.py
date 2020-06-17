import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
product_lists = []
for page in range(1, 100):
    res = requests.get(
        'https://www.coupang.com/np/campaigns/82/components/194176?page=' + str(page),
        headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    print(str(page) + '번 페이지 스크래핑 수행합니다.')

    try:
        li_list = soup.select_one('#productList').find_all('li')
    except:
        print('마지막 페이지입니다. 스크래핑 종료합니다.')
        break

    for li in li_list:
        product_lists.append([
            li.select_one('a > dl > dd > div.name').text.strip(),
            li.select_one('a > dl > dd > div.price-area > div > div.price > em > strong')
              .text.replace(',',''),
            li.select_one('a > dl > dd > div.other-info > div > span.rating-total-count')
              .text.strip()[1:-1]
        ])

# pprint.pprint(product_lists)
# csv, excel 로 저장 --> DB 테이블에 인서트
df = pd.DataFrame(product_lists, columns=['상품명', '가격', '좋아요 횟수'])
df.to_csv('coupang.csv')
df.to_excel('coupang.xlsx', encoding='cp949')
print('save ok..')


