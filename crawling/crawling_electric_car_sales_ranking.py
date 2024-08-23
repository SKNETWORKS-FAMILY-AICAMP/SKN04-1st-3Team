import pandas as pd
import psycopg2

from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

site_url = "https://tago.kr/model/order.htm"
driver.get(site_url)
bs = BeautifulSoup(driver.page_source, 'lxml')

data = bs.select("div.table-style.line table tbody tr td")

temp = [data[i].text for i in range(len(data)) if 1 <= i % 5 < 3]

car_names = [temp[i] for i in range(len(temp)) if i % 2 == 0]
sales = [temp[i] for i in range(len(temp)) if i % 2 == 1]

car_names_result = [car_names[j] for i in range(0, len(car_names), 10) for j in range(i, min(i+5, len(car_names)))]
sales_result = [sales[j] for i in range(0, len(sales), 10) for j in range(i, min(i+5, len(sales)))]
sales_result = [int(item.replace(',', '')) for item in sales_result]

dict_list = []
for i in range(0, len(car_names_result), 5):
    temp_dict = {car_names_result[j] : sales_result[j] for j in range(i, min(i+5, len(car_names_result)))}
    dict_list.append(temp_dict)

results = []
for i in range(0, 3):
    for key in dict_list[i]:
        present_value = dict_list[i][key]
        if key in dict_list[i+1]:
            previous_value = dict_list[i+1][key]
            diff = present_value - previous_value
            percentage_change = round((diff / previous_value) * 100, 2)
        else:
            percentage_change = 0.00

        results.append({
            '연도' : f"{2024-i}",
            '차종' : key,
            '판매대수' : present_value,
            '증감율(%)' : percentage_change
        })

df = pd.DataFrame(results)
print(df)

from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String, FLOAT
db_url = 'postgresql+psycopg2://postgres:1234@localhost:5432/electr_vehicle'

engine = create_engine(db_url, echo=True)

df.to_sql(
    'top_rank',
    engine,
    if_exists='replace', # replace: 덮어쓰기
    index=False,
    chunksize=5000,
    dtype={              # 데이터 열의 데이터 유형
            '연도': String,
            '차종': String,
            '판매대수': Integer,
            '증감율': FLOAT,
            
        }
    )