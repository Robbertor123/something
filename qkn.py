import requests
from bs4 import BeautifulSoup

rs = requests.get('https://kreekly.com/lists/2000-samyh-populyarnyh-angliyskih-slov/')
root = BeautifulSoup(rs.content, 'html.parser')

en_ru_items = []
q = root.find_all('span',class_='eng')
w=root.find_all('span',class_='rus')
e=len(q)
for i in range(e):
    print(q[i].text,w[i].text)