# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from openpyxl import Workbook

driver = webdriver.Chrome('chromeDriver')

def createCompanyInfo(company_link):
    url = 'https://thevc.kr' + company_link
    driver.get(url)

    html = driver.page_source
    soup_text = BeautifulSoup(html, "lxml")

    name = soup_text.h1.string
    info = soup_text.find(attrs={"class": "info_wrapper"})
    service = info.select("a > span")[0].string
    tech = info.select("p > span")[0].string
    category = info.select("p > span")[1].string + ' ∙ ' + info.select("p > span")[2].string
    content = info.select("span")[-1].string
    born = soup_text.find(attrs={"class": "basic_info"}).select("li:nth-of-type(5) > span")[0].string
    invested_money = soup_text.find(attrs={"class": "sum_invested"}).string
    invested_money = invested_money[:-1] + "00000000"
    contact_info = soup_text.find(attrs={"class": "contact_info"})
    email = contact_info.select("ul > li:nth-of-type(1) > span > a")[0].get('href')
    email = email[7:]
    tel = contact_info.select("ul > li:nth-of-type(2)) > span")[0].string
    link = contact_info.select("ul > li:nth-of-type(3)) > span > a")[0].get('href')

    return Company(name, service, tech, category, content, born, invested_money, email, tel, link, url)

def createExcel(company_list):
    wb = Workbook()
    ws = wb.active
    for company in company_list:
        ws.append(company)
    wb.save("company_info.xlsx")

class Company:
    def __init__(self, name, service, tech, category, content, born, invested_money, email, tel, link, url):
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
        self.url = url
