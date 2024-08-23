import json
import requests
from collections import OrderedDict
import pandas as pd
from sqlalchemy import create_engine
import psycopg2


API_KEY = 'YzFmMDk4ZDBhZjU0YjRlMWU2ZGQ2YjFjOTc5YWY4ZDc='

url = f'https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey={API_KEY}&itmId=13103873443T4+&objL1=ALL&objL2=13102873443B.0002+&objL3=13102873443C.0005+&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=M&startPrdDe=201512&endPrdDe=202407&outputFields=TBL_NM+OBJ_NM+NM+ITM_NM+UNIT_NM+PRD_DE+&orgId=116&tblId=DT_MLTM_5498'


response = requests.get(url)
results = json.loads(response.text)

target = ('201512', '201612', '201712', '201812', '201912', '202012', '202112', '202212', '202312')
set(target)

data = []

for i in range(len(results)):
    PRD_DE = results[i]['PRD_DE']
    count = int(results[i]['DT'])
    region = results[i]['C1_NM']

    if PRD_DE in target:
        PRD_DE = PRD_DE[:4]
        data.append([PRD_DE, count, region])

df = pd.DataFrame(data, columns=['year', 'value', 'region'])

from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String

db_url = 'postgresql+psycopg2://postgres:1234@localhost:5432/electr_vehicle'

engine = create_engine(db_url, echo=True)

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

    
    #with psycopg2.connect(
    #host='localhost',
    #dbname='electr_vehicle',
    #user='postgres',
    #password='1234',
    #port=5432,
    #) as conn:
        #with conn.cursor() as cur:
            #cur.execute(f'''INSERT INTO registerd_vehicle (id, region_name, registered_vehicles, date) VALUES ('{i+1}', '{region}','{count}','{formatted_date}')''')

    
    
    # DB만들어지면 연결예정
    # 2020-01부터 2024-02월기준 자료입니다

