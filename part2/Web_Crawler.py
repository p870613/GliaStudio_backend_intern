import requests
from bs4 import BeautifulSoup
def checkformat(soup, class_tag, index):
       content = soup.select(class_tag)[index].text
       return content

url = 'https://www.ptt.cc/bbs/graduate/M.1576159196.A.914.html'

resp = requests.get(url)

html_text = resp.text
soup = BeautifulSoup(html_text, 'lxml')

content = soup.find(id="main-content").text

date = checkformat(soup, '.article-meta-value', 3)
a = checkformat(soup, '.article-meta-value', 2)
b = checkformat(soup, '.article-meta-value', 0)
c = checkformat(soup, '.article-meta-value', 1)
print('標題', a)
print('作者', b)
print('看板', c)
print('時間',date)
target_content = u'※ 發信站: 批踢踢實業坊(ptt.cc),'
content = content.split(target_content)
print(len(content))
content = content[0].split(date)
main_content = content[1]
print('內文', main_content)


