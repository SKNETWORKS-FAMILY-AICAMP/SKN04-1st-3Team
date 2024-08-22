import json
import requests

API_KEY = 'YzFmMDk4ZDBhZjU0YjRlMWU2ZGQ2YjFjOTc5YWY4ZDc='

url = f'https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey={API_KEY}&itmId=13103873443T4+&objL1=ALL&objL2=13102873443B.0002+&objL3=13102873443C.0005+&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=M&startPrdDe=202001&endPrdDe=202402&outputFields=OBJ_NM+NM+ITM_NM+UNIT_NM+PRD_DE+&orgId=116&tblId=DT_MLTM_5498'


response = requests.get(url)
results = json.loads(response.text)




for i in range(len(results)):
    PRD_DE = int(results[i]['PRD_DE'])
    print(PRD_DE)
    
    
    
    # DB만들어지면 연결예정
    # 2020-01부터 2024-02월기준 자료입니다

