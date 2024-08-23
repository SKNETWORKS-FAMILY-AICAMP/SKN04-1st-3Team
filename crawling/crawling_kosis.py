import json
import requests
from collections import OrderedDict
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

def fetch_kosis_data():
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
    return df

