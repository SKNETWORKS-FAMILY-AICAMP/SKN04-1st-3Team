
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
driver.get(url="https://chargeinfo.ksga.org/front/statistics/evCar")
bs = BeautifulSoup(driver.page_source, 'lxml')

electric_car_count = bs.select('tbody td')[1:19]
total = [electric_car.text.replace('(', ' ').replace(')','').split() for electric_car in electric_car_count]

print(total)

#DB완성되면 연결예정