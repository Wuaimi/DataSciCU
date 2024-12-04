from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Q1(file_path): # DO NOT modify this line
    _TH_FULL_WEEKDAYS = {
    "วันจันทร์ที่" : 0,
    "วันอังคารที่" : 1,
    "วันพุธที่" : 2,    
    "วันพฤหัสบดีที่" : 3,
    "วันศุกร์ที่": 4,
    "วันเสาร์ที่": 5,
    "วันอาทิตย์ที่" : 6,
    }
    day_list = [0,0,0,0,0,0,0]
    with open(file_path) as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")
    all_bud_day = soup.select('div.bud-day')
    for one_month in all_bud_day:
        day = one_month.select('div.bud-day-col')[0].text.split(' ')[0]
        day_list[_TH_FULL_WEEKDAYS[day]] +=1
    return day_list


def Q2(file_path): # DO NOT modify this line
    with open(file_path) as f:
        html = f.read()
    soup = BeautifulSoup(html, "lxml")
    imp_day = soup.select('div.bud-day-col a')
    for day in imp_day:
        if day.get("title")=="วันวิสาขบูชา":
            vsk_day = day
    for node in vsk_day.parent.previous_siblings:
        if node.string.find("วัน")==0:
            ans = node.string    
    return ans

exec(input().strip()) # do not delete this linea