import pandas as pd
import psycopg2
import requests
import re

from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# def replace_spaces_with_single_dot_ignore_trailing(input_string):
#     # 문자열 마지막의 공백을 제거
#     stripped_string = input_string.rstrip()
    
#     # 공백을 .으로 대체
#     replaced_string = stripped_string.replace(' ', '.')
    
#     # 여러 개의 .을 하나의 .으로 대체
#     result_string = re.sub(r'\.+', '.', replaced_string)
    
#     return result_string

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# url = "https://www.hyundai.com/kr/ko/digital-customer-support/notice/notice/detail?pwiImtrSn=13205&page=1"
# response = requests.get(
#     url,
#     headers={'User-Agent': 'Mozilla 5.0'},
#     allow_redirects=True,
# )
# print(response)
# if response.status_code == 200:
#     bs = BeautifulSoup(response.text, 'lxml')

# print(type(bs))
# cars = bs.select("div.cont tr td")

# print(cars)

# 기아
# brand_url = "https://www.kia.com/kr/customer-service/notice/notice-202407311" # 브랜드 url
# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')
# table_url = "cmp-table__wrap grid-max spacing-pt6 spacing-pb8    fixed-scroll " # 테이블 url
# table_url = replace_spaces_with_single_dot_ignore_trailing(table_url)
# # print(url)
# cars = bs.select(f"div.{table_url} tr th")
# batteries = bs.select(f"div.{table_url} tr td")
# temp_cars = []
# temp_batteries = []
# for car in cars:
#     temp_cars.append(car.text)
# for battery in batteries:
#     temp_batteries.append(battery.text)

# print(temp_cars)
# print(temp_batteries)

#KG

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

# table_url = "cmp-embed"
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
# table_url = "nm-module nm-tbl-red"
# table_url = replace_spaces_with_single_dot_ignore_trailing(table_url)
# table_url
# table = bs.select(f"div.{table_url} tr td")
# table
# cars = [table[i] for i in range(2, len(table)) if i%2 == 0]
# batteries = [table[i] for i in range(2, len(table)) if i%2 == 1]
# for i in range(len(cars)):
#     print(cars[i].text, batteries[i].text)

# 폭스바겐
# brand_url = "https://www.volkswagen.co.kr/ko/Battery.html"

# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')
# table_url = "StyledContainer-sc-18harj2 eDqQLO"
# table_url = replace_spaces_with_single_dot_ignore_trailing("StyledContainer-sc-18harj2 eDqQLO")
# # table_url
# table = bs.select(f"div.{table_url} tr")
# table = table[1:]
# cars = []
# batteries = []
# for i in range(len(table)):
#     car, battery = table[i].text.split("/")
#     cars.append(car)
#     batteries.append(battery)
# for i in range(len(cars)):
#     print(cars[i], batteries[i])
