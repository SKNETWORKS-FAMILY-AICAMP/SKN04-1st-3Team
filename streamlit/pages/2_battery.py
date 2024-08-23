import streamlit as st
import pandas as pd

conn = st.connection('postgresql', type='sql')

st.title('내 자동차 배터리 제조사는?')

select_brand = st.selectbox(
    '확인하고 싶은 브랜드를 선택해주세요.',
    ['현대자동차 및 제네시스', '기아자동차', 'KG모빌리티', '르노', 'BMW', '벤츠', '아우디', '폭스바겐', '볼보', '스텔란티스(Jeep, 푸조, DS)', 
     '폴스타', '포르쉐', '토요타(렉서스)', '쉐보레', '재규어', '미니(BMW)', '롤스로이스', '지엠']
)

st.divider()

#브랜드별 차종과 배터리 제조사를 보여주는 쿼리입니당
# query = f"""
# SELECT 
#     public.electric_vehicle.vehicle_name AS vehicle_name, 
#     public.producer.producer_name AS producer_name,
#     public.brand.brand_name AS brand_name
# FROM 
#     public.brand
# JOIN 
#     public.electric_vehicle ON public.brand.brand_id = public.electric_vehicle.brand_id
# JOIN 
#     public.producer ON public.electric_vehicle.producer_id = public.producer.producer_id;
# """


query = """
SELECT 
    public.batery.car, 
    public.batery.battery
FROM 
    public.batery;
"""

df = conn.query(query, ttl=600)

#tmp_df = df[df['brand_name'] == select_brand]

# if df.empty:
#     st.write("선택한 브랜드에 대한 정보가 없습니다.")
# else:
#     st.table(df[['vehicle_name', 'producer_name']].rename(columns={'car': '차종', 'battery': '제조사'}))

if df.empty:
    st.write("배터리 정보가 없습니다.")
else:
    # 테이블로 표시
    st.table(df.rename(columns={'car': '차종', 'battery': '제조사'}))
