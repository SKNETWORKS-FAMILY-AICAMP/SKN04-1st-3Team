from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
# import crawling_kosis

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
driver.get(url = 'https://chargeinfo.ksga.org/front/statistics/evCar')
bs = BeautifulSoup(driver.page_source, 'lxml')

colunm = bs.select('thead')[0].text.strip('\n').split('\n')[:18]
colunm

# 초기 데이터 수집
electric_car_count = bs.select('tbody#tBodyList td')[:19]
total_initial = [int(electric_car.text.replace('(', ' ').replace(')', '').split()[0].replace(',', '')) for electric_car in electric_car_count]

# 데이터 리스트 초기화
data = [total_initial]

# 추가 데이터 수집
electric_car_count = bs.select('tbody#tBodyList td')

for start_index in range(38, len(electric_car_count), 19):
    total_batch = [int(electric_car.text.replace('(', ' ').replace(')', '').split()[0].replace(',', '')) for electric_car in electric_car_count[start_index-19:start_index]]
    data.append(total_batch)

# 2015년도까지
data = data[:10] 


# 칼럼과 맞지않는 총계 삭제
for row in data:
    if len(row) > len(colunm):
        row.pop()



total_electric = pd.DataFrame(data, columns=colunm)



df_long = pd.melt(total_electric, id_vars=['연월'], var_name='Region', value_name='Value')


from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String

db_url = 'postgresql+psycopg2://postgres:1234@localhost:5432/electric_vehicle'

engine = create_engine(db_url, echo=True)

df_long.to_sql(
  'electric_vehicles',
  engine,
  if_exists='replace', # replace: 덮어쓰기
  index=False,
  chunksize=5000,
  dtype={              # 데이터 열의 데이터 유형
      
        'year': String,
        'value': Integer,
        'region': String,
        
    }
)
