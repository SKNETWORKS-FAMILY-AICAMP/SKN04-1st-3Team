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

df = pd.DataFrame(data, columns=['연도', '값', '지역'])

regions = list(OrderedDict.fromkeys(df['지역']))

pivot_df = df.pivot(index='연도', columns='지역', values='값')

pivot_df = pivot_df[regions]

# 멀티인덱스 해제: 피벗된 데이터에서 칼럼 레이블 '지역'을 제거
pivot_df.columns.name = None

pivot_df = pivot_df.reset_index()

# 결과 확인
print(pivot_df)

        
from sqlalchemy import create_engine
from sqlalchemy.types import Integer, String

db_url = 'postgresql+psycopg2://postgres:1234@localhost:5432/electr_vehicle'

engine = create_engine(db_url, echo=True)

pivot_df.to_sql(
  'vehicle_data',
  engine,
  if_exists='replace', # replace: 덮어쓰기
  index=False,
  chunksize=5000,
  dtype={              # 데이터 열의 데이터 유형
        '연도': String,
        '서울': Integer,
        '부산': Integer,
        '대구': Integer,
        '인천': Integer,
        '광주': Integer,
        '대전': Integer,
        '울산': Integer,
        '세종': Integer,
        '경기': Integer,
        '강원': Integer,
        '충북': Integer,
        '충남': Integer,
        '전북': Integer,
        '전남': Integer,
        '경북': Integer,
        '경남': Integer,
        '제주': Integer,
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

