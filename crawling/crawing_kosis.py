import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
API_KEY = 'YzFmMDk4ZDBhZjU0YjRlMWU2ZGQ2YjFjOTc5YWY4ZDc='

url = f'https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey={API_KEY}&itmId=13103873443T4+&objL1=ALL&objL2=13102873443B.0002+&objL3=13102873443C.0005+&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=M&newEstPrdCnt=1&outputFields=TBL_NM+OBJ_NM+NM+ITM_NM+UNIT_NM+&orgId=116&tblId=DT_MLTM_5498'

response = requests.get(url)
results = json.loads(response.text)

for i in range(len(results)):
    count = int(results[i]['DT'])
    region = results[i]['C1_NM']
    
    print(count) # 차량수
    print(region) # 지역명 

    # DB만들어지면 연결예정

