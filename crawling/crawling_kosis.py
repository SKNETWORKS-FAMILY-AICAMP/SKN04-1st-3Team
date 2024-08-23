import json
import requests
import psycopg2

API_KEY = 'YzFmMDk4ZDBhZjU0YjRlMWU2ZGQ2YjFjOTc5YWY4ZDc='

url = f'https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey={API_KEY}&itmId=13103873443T4+&objL1=ALL&objL2=13102873443B.0002+&objL3=13102873443C.0005+&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=M&startPrdDe=201512&endPrdDe=202407&outputFields=TBL_NM+OBJ_NM+NM+ITM_NM+UNIT_NM+PRD_DE+&orgId=116&tblId=DT_MLTM_5498'


response = requests.get(url)
results = json.loads(response.text)

target = ('201512', '201612', '201712', '201812', '201912', '202012', '202112', '202212', '202312')
set(target)


for i in range(len(results)):
    PRD_DE = results[i]['PRD_DE']
    count = results[i]['DT']
    region = results[i]['C1_NM']

    formatted_date = f"{PRD_DE[:4]}-{PRD_DE[4:6]}-01"

    if PRD_DE in target:
        PRD_DE = int(PRD_DE[:4])
        print(PRD_DE, count, region)

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

