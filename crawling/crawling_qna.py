from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import requests

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

FAQ = []

#Q1
Q = '우리나라의 전기차 이용 비율은 높아지고 있나요?'
url = 'https://www.investkorea.org/ik-kr/cntnts/i-3022/web.do?clickArea=krmain00023'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')
A = bs.select('div.ig_content > div.sub-section')[3].text.split('\t\t\t\t\t\t')
FAQ.append({
    'Question': Q,
    'Answer': A
})

#Q2
Q = '세계 전기차 배터리 회사에는 어떤 것들이 있나요?'
url = 'https://www.investkorea.org/ik-kr/cntnts/i-3022/web.do?clickArea=krmain00023'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')
A = bs.select('div.img-box > img')[1]
FAQ.append({
    'Question': Q,
    'Answer': A
})

#Q3
Q = '전기차 구매시 보조금은 어떻게 되나요'
url = 'https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1404&ccfNo=2&cciNo=1&cnpClsNo=1'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')
A = bs.select('div.tplv5')[0].text
FAQ.append({
    'Question': Q,
    'Answer': A
})

#Q4
Q = '해외에서 우리나라의 전기차 배터리 회사 순위'
url = 'https://www.g-enews.com/article/Industry/2024/04/2024041510303417377bdb7041ec_1'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')
A = bs.select('div.vtxt.detailCont')[0].text.split('. ')[3]
FAQ.append({
    'Question': Q,
    'Answer': A
})

#Q5
Q = '국적별 배터리 생산 능력 점유율 전망은 어떻게 되나요'
url = 'https://www.investkorea.org/ik-kr/cntnts/i-3022/web.do?clickArea=krmain00023'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')
A = bs.select('div.img-box > img')[0]
FAQ.append({
    'Question': Q,
    'Answer': A
})

#Q6
Q = '지역별 인당 차량 등록대수는 어떻게 되나요'
url = 'https://www.medicalworldnews.co.kr/m/view.php?idx=1510956612'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')
A = bs.select('strong.title')[0].text
FAQ.append({
    'Question': Q,
    'Answer': A
})

#Q7
Q = '성별에 따른 자동차 등록현황을 보여주세요'
url = 'https://www.bigdata-map.kr/datastory/new/story_54'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')
A = bs.select('div.img-wrap')[6]
FAQ.append({
    'Question': Q,
    'Answer': A
})