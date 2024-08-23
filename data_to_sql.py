from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String
import psycopg2
from psycopg2 import sql
from crawling.crawling_electric_car_sales_ranking import fetch_car_sales_data
from crawling.crawling_kosis import fetch_kosis_data
from crawling.crawling_electric_car import fetch_car_data
from crawling.crawling_batteries import fetch_

# 1. 기본 데이터베이스에 연결 (예: 'postgres')
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1234",
    host='localhost',
    port="5432"
)
conn.autocommit = True  # Auto-commit을 활성화하여 데이터베이스 생성 쿼리가 즉시 실행되도록 설정

cursor = conn.cursor()

# 2. 필요한 데이터베이스 생성 (예: 'my_database')
database_name = "electr_vehicle"
cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name)))

# 3. 연결을 종료하고 생성한 데이터베이스로 다시 연결
cursor.close()
conn.close()

db_url = 'postgresql+psycopg2://postgres:1234@localhost:5432/postgres'

engine = create_engine(db_url, echo=True)

vehicle_data = fetch_kosis_data()
electric_vehicles = fetch_car_data()
battery = fetch_()


df.to_sql(
  'vehicle_data',
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
    