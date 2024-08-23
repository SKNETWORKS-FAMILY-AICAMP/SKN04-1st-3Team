import re
import pandas as pd
import psycopg2

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

# conn = psycopg2.connect(
#     host='localhost',
#     database='postgres',
#     user='postgres',
#     password='9708'
# )
# cursor = conn.cursor()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

temp_cars = []
temp_batteries = []
urls = {}

# 현대자동차 및 제네시스
# 500 error
# 배터리 제조사가 세군데인 차량 존재

# brand_url = "https://www.hyundai.com/kr/ko/digital-customer-support/notice/notice/detail?pwiImtrSn=13205&page=1"
# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')

# table = bs.select("div.cont tbody td")

# cars = []
# batteries = []

# for i in range(2, len(table)):
#     if i>=9 and i<12:
#         batteries.append(table[i].text.strip())
#         continue
    
#     if i%2 == 0:
#         cars.append(table[i].text.strip())
#     elif i%2 == 1:
#         batteries.append(table[i].text.strip())



# 기아

brand_url = "https://www.kia.com/kr/customer-service/notice/notice-202407311"
driver.get(brand_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

table_class = "cmp-table__wrap grid-max spacing-pt6 spacing-pb8    fixed-scroll "
table_class = replace_spaces(table_class)

cars = bs.select(f"div.{table_class} tbody th")
batteries = bs.select(f"div.{table_class} tbody td")

cars_ = [car.text.strip().replace("\xa0", "") for car in cars]
batteries_ = [battery.text.strip().replace("\xa0", "") for battery in batteries]

temp_cars.extend(cars_)
temp_batteries.extend(batteries_)
urls.update({"kia" : f"{brand_url}"})



# KG 모빌리티
# url problem : 세부 페이지 X


# 르노

brand_url = "https://www.renault.co.kr/ko/inside/notice_view.jsp?idx=18&update2=2024-08-13" # 브랜드 url
driver.get(brand_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

table = bs.select("div.tbl_wrap tr td")
cars = [table[i].text.strip() for i in range(len(table)) if i%2 == 0]
batteries = [table[i].text.strip() for i in range(len(table)) if i%2 == 1]

temp_cars.extend(cars)
temp_batteries.extend(batteries)
urls.update({"renault" : f"{brand_url}"})



# BMW

brand_url = "https://www.bmw.co.kr/ko/bmw-korea/privacy-policy/notice-new.html"
driver.get(brand_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

table_class = "cmp-embed"
table = bs.select("div.cmp-embed td")
cars = [table[i].text.strip() for i in range(2, len(table)) if i%2 == 0]
batteries = [table[i].text.strip() for i in range(2, len(table)) if i%2 == 1]

temp_cars.extend(cars)
temp_batteries.extend(batteries)
urls.update({"bmw" : f"{brand_url}"})



# 벤츠
# bs까지는 출력되나 select() 되지않음

# brand_url = "https://www.mercedes-benz.co.kr/passengercars/electric-battery.html"
# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')

# table_class = "wb-grid-container"
# table = bs.select("div.wb-grid-container")
# table

# print(len(cars), len(batteries))
# temp_cars.extend(cars)
# temp_batteries.extend(batteries)



# 아우디

brand_url = "https://www.audi.co.kr/kr/web/ko/aboutaudi/customerinfo/evbattery.html"
driver.get(brand_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

table_class = "nm-module nm-tbl-red"
table_class = replace_spaces(table_class)
table = bs.select(f"div.{table_class} tr td")

cars = [table[i].text.strip() for i in range(2, len(table)) if i%2 == 0]
batteries = [table[i].text.strip() for i in range(2, len(table)) if i%2 == 1]

temp_cars.extend(cars)
temp_batteries.extend(batteries)
urls.update({"audi" : f"{brand_url}"})



# 폭스바겐
# 사이트 로그인을 해야함 (driver.get()을 했을 시)

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
# url problem : 세부 페이지 X



# JEEP
# bs까지는 출력되나 select() 되지않음

# brand_url = "https://www.jeep.co.kr/notice.html"
# driver.get(brand_url)
# bs = BeautifulSoup(driver.page_source, 'lxml')

# table = bs.select("div.tls")
# table



# 테슬라
# url problem



# 폴스타
# 폴스타2, 폴스타4 두 차량의 url이 각각 존재
# 또한 각 차량에 대해 싱글 모터, 듀얼 모터 두 가지 버전 존재

brand_url = "https://www.polestar.com/kr/polestar-2/specifications/#charging"
driver.get(brand_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

table_cars = bs.select("tr.css-1xdhyk6 th")
table_batteries = bs.select("p.css-11zwe5n") # table[22], table[23]

cars = [table_cars[2].text, table_cars[3].text]
batteries = [table_batteries[22].text, table_batteries[23].text]

temp_cars.extend(cars)
temp_batteries.extend(batteries)
urls.update({"polestar2" : f"{brand_url}"})





# 포르쉐
# 빈 리스트 반환할 때 있음
# select() -> p-text / p-text.hydrated

brand_url = "https://www.porsche.com/korea/ko/accessoriesandservice/bev-battery-notice/"
driver.get(brand_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

table_class = "PcomGrid__grid__f560b TextContent__double__a2a42"
table_class = replace_spaces(table_class)

table = bs.select(f"div.{table_class} p-text")
cars = [table[i].text.strip() for i in range(len(table)) if i%2 == 0]
batteries = [table[i].text.strip() for i in range(len(table)) if i%2 == 1]

temp_cars.extend(cars)
temp_batteries.extend(batteries)
urls.update({"porsche" : f"{brand_url}"})



# 렉서스

brand_url = "https://www.lexus.co.kr/contents/electric-battery-notice/"
driver.get(brand_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

table = bs.select("table.d-block-pc tbody td")

cars = [table[i].text.strip() for i in range(len(table)) if i%2 == 0]
batteries = [table[i].text.strip() for i in range(len(table)) if i%2 == 1]

temp_cars.extend(cars)
temp_batteries.extend(batteries)
urls.update({"lexus" : f"{brand_url}"})



# 쉐보레
# img file -> 직접 입력

brand_url = "https://www.chevrolet.co.kr/events/ev-information"
driver.get(brand_url)

cars = ["BOLT EUV", "BOLT EV"]
model_years = ["MY22 ~ MY23", "MY17 ~ MY23"]
cars_with_model_year = [cars[i] + " " + model_years[i] for i in range(len(cars))]
batteries = ["LG에너지솔루션", "LG에너지솔루션"]



# 재규어
# url problem



# 미니(BMW)

brand_url = "https://www.mini.co.kr/ko_KR/home/news-and-brand/news/MINI-electric-car-maufacturer.html"
driver.get(brand_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

table = bs.select("table.table-item tbody td")
cars = [table[i].text.strip() for i in range(len(table)) if i%2 == 0]
batteries = [table[i].text.strip() for i in range(len(table)) if i%2 == 1]

temp_cars.extend(cars)
temp_batteries.extend(batteries)
urls.update({"mini" : f"{brand_url}"})



# 롤스로이스
# url problem



# 지엠
# 모델명과 연식 문자열 덧붙여 cars_with_model_year에 저장

brand_url = "https://www.cadillac.co.kr/events/batteryannouncement"
driver.get(brand_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

table = bs.select(f"div.col-con div.col-con div.col-con p")

cars = [table[i].text.strip() for i in range(3, len(table)) if i%3 == 0]
model_years = [table[i].text.strip() for i in range(3, len(table)) if i%3 == 1]
cars_with_model_year = [cars[i] + " " + model_years[i] for i in range(len(cars))]
batteries = [table[i].text.strip() for i in range(3, len(table)) if i%3 == 2]

temp_cars.extend(cars_with_model_year)
temp_batteries.extend(batteries)
urls.update({"gm" : f"{brand_url}"})

print(len(temp_cars), len(temp_batteries), len(urls))

# data_cars_batteries = {
#     'car' : temp_cars,
#     'battery' : temp_batteries
# }

# df = pd.DataFrame(data_cars_batteries)
