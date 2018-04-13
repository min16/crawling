import requests
from bs4 import BeautifulSoup

html = open('index.html', 'r', encoding='UTF8').read()
soup = BeautifulSoup(html, 'lxml')
# print(soup)

content_table = soup.table
link_list = []
for a_link in content_table.find_all('a'):
    link_list.append(a_link.get('href'))

# for link in link_list:
# url = 'https://thevc.kr/' + str(link_list[0])
url = 'https://thevc.kr/' + 'Solmedix'
source_code = requests.get(url)
plain_text = source_code.text
soup_text = BeautifulSoup(plain_text, 'lxml')
name
service
tech
part
content
born
invested_money
email
tel = soup_text.find(attrs={"class": "contact_info"}).select("ul > li:nth-of-type(2)) > span")[0].string
link = soup_text.find(attrs={"class": "contact_info"}).select("ul > li:nth-of-type(3)) > span > a")[0].get('href')

print(company_link, phone)
#print(soup_text)

def getCompanyInfo(company_link):
    url = 'https://thevc.kr/' + 'Solmedix'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup_text = BeautifulSoup(plain_text, 'lxml')

    name
    service
    tech
    category
    content
    born
    invested_money
    email
    tel = soup_text.find(attrs={"class": "contact_info"}).select("ul > li:nth-of-type(2)) > span")[0].string
    link = soup_text.find(attrs={"class": "contact_info"}).select("ul > li:nth-of-type(3)) > span > a")[0].get('href')

    return Company(name, service, tech, category, content, born, invested_money, email, tel, link)

class Company:
    def __init__(self, name, service, tech, category, content, born, invested_money, email, tel, link):
        self.name = name
        self.service = service
        self.tech = tech
        self.category = category
        self.content = content
        self.born = born
        self.invested_money = invested_money
        self.email = email
        self.tel = tel
        self.link = link
