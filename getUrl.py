# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
from bs4 import BeautifulSoup


def getUrl(file_name):
    html = open(file_name, 'r', encoding='UTF8').read()
    soup = BeautifulSoup(html, "lxml")
    content_table = soup.find_all(attrs={"class": "content-row"})

    link_list = []
    for row in content_table:
        link = row.select("td:nth-of-type(6) > div > a")[0].get('href')
        money = row.find(attrs={"class": "amount"}).string
        if money == "비공개":
            continue
        money = float(money[:-1])
        # 중복없이 투자금액 100억이하, 5억 이하일 경우에만 기업리스트에 추가
        if money > 100.0 or money < 5.0 or link in link_list:
            continue
        link_list.append(link)
    # print(link_list)
    return link_list
