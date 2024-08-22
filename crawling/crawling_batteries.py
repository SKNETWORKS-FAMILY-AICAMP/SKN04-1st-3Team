import pandas as pd
import psycopg2
import requests
import re

from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def replace_spaces(input_string):

    result = input_string.strip().replace(' ', '.') 
    # 여러 개의 .을 하나의 .으로 대체
    result = re.sub(r'\.+', '.', result)
    
    return result

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 현대자동차 및 제네시스
# 500 err

url = "https://www.hyundai.com/kr/ko/digital-customer-support/notice/notice/detail?pwiImtrSn=13205&page=1"

# 기아

brand_url = "https://www.kia.com/kr/customer-service/notice/notice-202407311" # 브랜드 url
driver.get(brand_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

table_class = "cmp-table__wrap grid-max spacing-pt6 spacing-pb8    fixed-scroll " # 테이블 url
table_class = replace_spaces(table_class)

cars = bs.select(f"div.{table_class} tbody th")
batteries = bs.select(f"div.{table_class} tbody td")

cars_ = [car.text.replace("\xa0", "") for car in cars]
batteries_ = [battery.text.replace("\xa0", "") for battery in batteries]


# KG

# 르노
# brand_url = "https://www.renault.co.kr/ko/inside/notice_view.jsp?idx=18&update2=2024-08-13" # 브랜드 url
# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')
# # table_url = "tbl_wrap"
# # bs
# table = bs.select("div.tbl_wrap tr td")
# cars = [table[i] for i in range(len(table)) if i%2 == 0]
# batteries = [table[i] for i in range(len(table)) if i%2 == 1]
# # print(len(cars), len(batteries))
# # for i in range(len(cars)):
# #     print(cars[i].text, batteries[i].text)

# BMW
# brand_url = "https://www.bmw.co.kr/ko/bmw-korea/privacy-policy/notice-new.html"
# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')

# table_class = "cmp-embed"
# table = bs.select("div.cmp-embed tr td")
# cars = [table[i] for i in range(2, len(table)) if i%2 == 0]
# batteries = [table[i] for i in range(2, len(table)) if i%2 == 1]
# for i in range(len(cars)):
#     print(cars[i].text, batteries[i].text)

# 벤츠


# 아우디
# brand_url = "https://www.audi.co.kr/kr/web/ko/aboutaudi/customerinfo/evbattery.html"

# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')
# table_class = "nm-module nm-tbl-red"
# table_class = replace_spaces(table_class)
# table_class
# table = bs.select(f"div.{table_class} tr td")
# table
# cars = [table[i] for i in range(2, len(table)) if i%2 == 0]
# batteries = [table[i] for i in range(2, len(table)) if i%2 == 1]
# for i in range(len(cars)):
#     print(cars[i].text, batteries[i].text)

# 폭스바겐
# brand_url = "https://www.volkswagen.co.kr/ko/Battery.html"

# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')
# table_class = "StyledContainer-sc-18harj2 eDqQLO"
# table_class = replace_spaces("StyledContainer-sc-18harj2 eDqQLO")
# # table_url
# table = bs.select(f"div.{table_class} tr")
# table = table[1:]
# cars = []
# batteries = []
# for i in range(len(table)):
#     car, battery = table[i].text.split("/")
#     cars.append(car)
#     batteries.append(battery)
# for i in range(len(cars)):
#     print(cars[i], batteries[i])

# 볼보
# url problem

# JEEP


# 테슬라
# 이상함

# 폴스타
# 사이트 2개로 나누어져있음

# 포르쉐
# 문제있음
# brand_url = "https://www.porsche.com/korea/ko/accessoriesandservice/bev-battery-notice/"

# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')

# table_class = "PcomGrid__grid__f560b TextContent__double__a2a42"
# table_class = replace_spaces(f"{table_class}")

# table = bs.select(f"div.{table_class}")
# len(table)


# 렉서스

# brand_url = "https://www.lexus.co.kr/contents/electric-battery-notice/"

# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')

# table = bs.select("table.d-block-pc tr td")
# cars = []
# batteries = []

# cars = [table[i].text.strip() for i in range(len(table)) if i%2 == 0]
# batteries = [table[i].text.strip() for i in range(len(table)) if i%2 == 1]
# for i in range(len(cars)):
#     print(cars[i], batteries[i])

# 쉐보레
# img파일임;
# brand_url = "https://www.chevrolet.co.kr/events/ev-information"

# driver.get(brand_url)

# 재규어
# ?

# 미니(BMW)
# brand_url = "https://www.mini.co.kr/ko_KR/home/news-and-brand/news/MINI-electric-car-maufacturer.html"

# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')

# table = bs.select("table.table-item span.md-heading.md-fixedtext")

# cars = []
# batteries = []

# cars = [table[i].text.strip() for i in range(1, len(table)) if i%2 == 0]
# batteries = [table[i].text.strip() for i in range(1, len(table)) if i%2 == 1]
# for i in range(len(cars)):
#     print(cars[i])
#     print(batteries[i])

# 롤스로이스


# 지엠
# brand_url = "https://www.cadillac.co.kr/events/batteryannouncement"
# driver.get(brand_url)

# bs = BeautifulSoup(driver.page_source, 'lxml')

# # table_url = "col-sm-12 col-sm-gut-no "
# # table_url = replace_spaces_with_single_dot_ignore_trailing(table_url)

# table = bs.select(f"div.gb-body1")
# table = table[1:-1]
# len(table)
# cars = [table[i].text.strip() for i in range(3, len(table)) if i%3 == 0]
# years = [table[i].text.strip() for i in range(3, len(table)) if i%3 == 1]
# batteries = [table[i].text.strip() for i in range(3, len(table)) if i%3 == 2]

# cars = [cars[i] + " " + years[i] for i in range(len(cars))]
# # len(cars)
# for i in range(len(cars)):
#     print(cars[i])
#     print(batteries[i])

