import requests

res = requests.get('https://thumbnail6.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/2019/10/29/12/2/2b6c8fbb-106d-4732-b093-69cb4eeb6c70.jpg')

with open('test.jpg', 'wb') as f:
    f.write(res.content)

print('저장완료')
