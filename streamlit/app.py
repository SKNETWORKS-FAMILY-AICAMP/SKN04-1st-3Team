import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import time

# 데이터 로딩
@st.cache
def load_data():
    df = pd.DataFrame(data = {
        'Month' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'region': ['서울특별시', '경기도', '인천광역시', '부산광역시', '대구광역시', '대전광역시', '광주광역시', '울산광역시', '강원도', '충청북도', '충청남도', '전라북도'],
        'value': [50000, 45000, 30000, 28000, 26000, 22000, 20000, 18000, 17000, 16000, 15000, 14000]
    })
    return df

data = load_data()

months = sorted(data['Month'].unique())
num_months = len(months)

# 프로그레스 바와 버튼 생성
progress_bar = st.progress(0)
start_button = st.button("Start")

if start_button:
    for i in range(num_months):
        selected_month = months[i]
        filtered_data = data[data['Month'] == selected_month]

        # 지도 생성
        m = folium.Map(location=[filtered_data['Latitude'].mean(), filtered_data['Longitude'].mean()], zoom_start=10)

        for _, row in filtered_data.iterrows():
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=row['Info']
            ).add_to(m)

        # Streamlit에서 Folium 지도 표시
        st_folium(m, width=700, height=500)
        
        progress_bar.progress((i + 1) / num_months)
        time.sleep(1)  # 업데이트 주기를 설정 (1초)
