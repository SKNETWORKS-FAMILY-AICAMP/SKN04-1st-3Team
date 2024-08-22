
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
driver.get(url = 'https://chargeinfo.ksga.org/front/statistics/evCar')
bs = BeautifulSoup(driver.page_source, 'lxml')

colunm = bs.select('thead')[0].text.strip('\n').split('\n')[:18]
colunm

# 초기 데이터 수집
electric_car_count = bs.select('tbody#tBodyList td')[:19]
total_initial = [electric_car.text.replace('(', ' ').replace(')', '').split()[0] for electric_car in electric_car_count]

# 데이터 리스트 초기화
data = [total_initial]

# 추가 데이터 수집
electric_car_count = bs.select('tbody#tBodyList td')

for start_index in range(38, len(electric_car_count), 19):
    total_batch = [electric_car.text.replace('(', ' ').replace(')', '').split()[0] for electric_car in electric_car_count[start_index-19:start_index]]
    data.append(total_batch)

# 2015년도까지
data = data[:10] 

# 칼럼과 맞지않는 총계 삭제
for row in data:
    if len(row) > len(colunm):
        row.pop()

total_electric = pd.DataFrame(data, columns=colunm)

print(total_electric)

#DB완성되면 연결예정