import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import json

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.header('자동차 등록대수')
st.divider()
#-------------------

st.subheader('시도 별 자동차 등록대수')
latitude = 36.5
longitude = 127.5

geo_path = 'SIDO_MAP.json'

# JSON 파일을 UTF-8 인코딩으로 읽기
with open(geo_path, encoding='utf-8') as f:
    geo_data = json.load(f)

data = {
    'region': ['서울특별시', '경기도', '인천광역시', '부산광역시', '대구광역시', '대전광역시', '광주광역시', '울산광역시', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도'],
    'value': [50000, 45000, 30000, 28000, 26000, 22000, 20000, 18000, 17000, 16000, 15000, 14000, 13000, 12000, 11000, 10000]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 지도 생성
m = folium.Map(location=[latitude, longitude], zoom_start=7)

# Choropleth 생성
folium.Choropleth(
    geo_data=geo_data,
    name='choropleth',
    data=df,
    columns=['region', 'value'],
    key_on='feature.properties.CTP_KOR_NM',
    fill_color='YlOrRd',  # 값에 따라 색상이 노란색에서 빨간색으로 변합니다.
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='자동차 등록대수'
).add_to(m)

# 시도별 경계선 추가
folium.GeoJson(
    geo_data,
    name='geojson',
    style_function=lambda feature: {
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.1
    }
).add_to(m)

# 지도에 경계선 추가
folium.LayerControl().add_to(m)

st.components.v1.html(m._repr_html_(), width=800, height=600)
st.divider()
#-------------------

st.subheader('년도 별 차량/전기차 등록대수 현황')
years = np.arange(2020, 2025)
vehicle_registrations = np.random.randint(100000, 200000, size=len(years)).cumsum()
ev_registrations = np.random.randint(10000, 50000, size=len(years)).cumsum()

df = pd.DataFrame({
    'Year': years,
    'Vehicle Registrations': vehicle_registrations,
    'EV Registrations': ev_registrations
})

fig, ax = plt.subplots()
ax.plot(df['Year'], df['Vehicle Registrations'], label='차량 등록대수', marker='o')
ax.plot(df['Year'], df['EV Registrations'], label='전기차 등록대수', marker='o')
ax.set_xlabel('년도')
ax.set_ylabel('등록대수')
ax.set_title('2020~2024년 차량/전기차 등록대수 현황')
ax.legend()

st.pyplot(fig)