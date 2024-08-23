# from crawling.crawling_electric_car_sales_ranking import fetch_car_sales_data
# from crawling.crawling_kosis import fetch_kosis_data
from crawling.crawling_electric_car import fetch_car_data
# df = fetch_car_sales_data()
# df1 = fetch_kosis_data()
df2 = fetch_car_data()

print(df2)