import streamlit as st
from streamlit_echarts import st_echarts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import json
import altair as alt
from sqlalchemy import create_engine

# Streamlit 페이지 설정
st.set_page_config(
    page_title="자동차 등록대수 현황",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 스타일 테마 설정
alt.themes.enable("dark")

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.header('자동차 등록대수')
st.divider()
#-------------------

st.subheader('년도 별 차량/전기차 등록대수 현황')

# 데이터 로드
conn = st.connection('postgresql', type='sql')

query = f"""
SELECT 
    public.vehicle_data.year AS year, 
    public.vehicle_data.value AS registered,
    public.vehicle_data.region AS region
FROM 
    public.vehicle_data
"""

df_car = conn.query(query, ttl=600)

df_car_pivot = df_car.pivot(index='year', columns='region', values='registered').reset_index()

df_car_pivot['year'] = df_car_pivot['year'].astype('int')

df_car_pivot['total'] = df_car_pivot.iloc[:,1:].sum(axis=1)/10000

query = f"""
SELECT 
    "연월" AS year, 
    public.electric_vehicles."Value" AS registered,
    public.electric_vehicles."Region" AS region
FROM 
    public.electric_vehicles
"""

df_ecar = conn.query(query, ttl=600)

df_ecar_pivot = df_ecar.pivot(index='year', columns='region', values='registered').reset_index()

df_ecar_pivot['total'] = df_ecar_pivot.iloc[:,1:].sum(axis=1)/10000


# ECharts 옵션 설정
options = {
    "tooltip": {
        "trigger": 'axis',
        "axisPointer": {
            "type": 'cross'
        }
    },
    "legend": {
        "data": ['Total Vehicles', 'Electric Vehicles']
    },
    "xAxis": {
        "type": 'category',
        "boundaryGap": False,
        "data": df_car_pivot['year'].to_list()
    },
    "yAxis": {
        "type": 'value'
    },
    "series": [
        {
            "name": 'Total Vehicles',
            "type": 'line',
            "data": df_car_pivot['total'].to_list(),
            "smooth": True,
        },
        {
            "name": 'Electric Vehicles',
            "type": 'line',
            "data": df_ecar_pivot['total'].to_list(),
            "smooth": True,
        }
    ]
}

# Streamlit 애플리케이션에서 그래프 표시
st.title("Vehicle Registration Trends (2015 - 2023)")
st.write("Total vehicle registrations and electric vehicle registrations from 2015 to 2023.")

# ECharts 그래프 렌더링
st_echarts(options=options)

st.divider()

# 데이터 로드 (예시 데이터 경로 및 읽기)
geo_path = 'SIDO_MAP.json'
with open(geo_path, encoding='utf-8') as f:
    geo_data = json.load(f)

# 데이터 필터링
# 데이터 구성
# df_cars = pd.merge(df_car, df_ecar, how='left', on='year', suffixes=('_car', '_elec_car'))

# Sidebar 설정
with st.sidebar:
    st.title('🚗 Korea Dashboard')
    
    year_list = list(df_ecar['year'].unique())[::-1]
    selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
    df_selected_year = df_ecar[df_ecar['year'] == selected_year]
    df_selected_year_sorted = df_selected_year.sort_values(by="registered", ascending=False)[:5]

# Streamlit에서 2개의 컬럼 생성
col = st.columns((0.2, 0.8), gap='medium')

# 지도 그리기
with col[0]:
    st.markdown('#### Top States')

    st.dataframe(df_selected_year_sorted,
                 column_order=("region", "registered"),
                 hide_index=True,
                 width=None)

with col[1]:
    st.subheader('시도 별 자동차 등록대수')
    latitude = 36.2
    longitude = 127.5

    # 지도 생성
    m = folium.Map(location=[latitude, longitude],
                   zoom_start=6,
                   zoom_control=False,
                   tiles=None, 
                   dragging=False,
                   scrollWheelZoom=False,
                   doubleClickZoom=False)

    folium.TileLayer('cartodbpositron').add_to(m)

    # 색상 스케일 설정
    color_scale = folium.LinearColormap(colors=['#FFEDA0', '#FEB24C', '#F03B20'], 
                                        vmin=df_ecar['registered'].min(), 
                                        vmax=df_ecar['registered'].max())
    
    # GeoJSON 데이터와 데이터프레임 결합하여 지도에 데이터 추가
    for feature in geo_data['features']:
        region_name = feature['properties']['CTP_KOR_NM']
        if ('북도' in region_name) or ('남도' in region_name):
            region_name = region_name[0]+region_name[2]
        else:
            region_name = region_name[:2]
            
        region_data = df_selected_year[df_selected_year['region'] == region_name]
        if not region_data.empty:
                value = region_data['registered'].iloc[0]
                color = color_scale(value)
            
                folium.GeoJson(
                    feature,
                    style_function=lambda x, color=color: {
                        'fillColor': color,
                        'color': 'black',
                        'weight': 1,
                        'fillOpacity': 0.7,
                    },
                    tooltip=folium.Tooltip(f"{region_name}: {value}"),
                    highlight_function=lambda x: {'color': 'white', 'weight': 3, 'fillOpacity': 0.9}
                ).add_to(m)
        
    color_scale.add_to(m)
    st.components.v1.html(m._repr_html_(), width=570, height=900)


st.divider()


# with st.sidebar:
#     
    
#     year_list = list(df_reshaped.year.unique())[::-1]
    
#     selected_year = st.selectbox('Select a year', year_list, index=len(year_list)-1)
#     df_selected_year = df_reshaped[df_reshaped.year == selected_year]
#     df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)

#     color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
#     selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

# # Streamlit에서 2개의 컬럼 생성
# col = st.columns((0.8, 0.2), gap='medium')
# with col[0]:
#     st.subheader('시도 별 자동차 등록대수')
#     latitude = 36.2
#     longitude = 127.5
#     # southwest = [33.0, 126.0]  # 대한민국 남서쪽 경계
#     # northeast = [39.0, 129.0]  # 대한민국 북동쪽 경계

#     # 지도 데이터 로드
#     geo_path = 'SIDO_MAP.json'  # GeoJSON 파일 경로

#     # JSON 파일을 UTF-8 인코딩으로 읽기
#     with open(geo_path, encoding='utf-8') as f:
#         geo_data = json.load(f)

#     data = {
#         'region': ['서울특별시', '경기도', '인천광역시', '부산광역시', '대구광역시', '대전광역시', '광주광역시', '울산광역시', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도'],
#         'value': [50000, 45000, 30000, 28000, 26000, 22000, 20000, 18000, 17000, 16000, 15000, 14000, 13000, 12000, 11000, 10000]
#     }

#     # 데이터프레임 생성
#     df = pd.DataFrame(data)

#     # 지도 생성
#     m = folium.Map(location=[latitude, longitude],
#                    zoom_start=6,
#                    zoom_control=False,
#                    tiles=None, 
#                    dragging=False,
#                    scrollWheelZoom=False,
#                    doubleClickZoom=False)

    
#     # # # 지도 경계 설정
#     # m.fit_bounds([southwest, northeast])
    
#     folium.TileLayer('cartodbpositron').add_to(m)
    
    

#     # 색상 스케일 설정
#     color_scale = folium.LinearColormap(colors=['#FFEDA0', '#FEB24C', '#F03B20'], 
#                                         vmin=df['value'].min(), 
#                                         vmax=df['value'].max())

#     # GeoJSON 데이터와 데이터프레임 결합하여 지도에 데이터 추가
#     for feature in geo_data['features']:
#         region_name = feature['properties']['CTP_KOR_NM']
#         region_data = df[df['region'] == region_name]
        
#         if not region_data.empty:
#             value = region_data['value'].iloc[0]
#             color = color_scale(value)
            
#             folium.GeoJson(
#                 feature,
#                 style_function=lambda x, color=color: {
#                     'fillColor': color,
#                     'color': 'black',
#                     'weight': 1,
#                     'fillOpacity': 0.7,
#                 },
#                 tooltip=folium.Tooltip(f"{region_name}: {value}"),
#                 highlight_function=lambda x: {'color': 'white', 'weight': 3, 'fillOpacity': 0.9}
#             ).add_to(m)
    
#     # 
#     color_scale.add_to(m)
        
#     # 지도에 경계선 추가
#     folium.LayerControl().add_to(m)
    
#     st.components.v1.html(m._repr_html_(), width=570, height=900)

# with col[1]:
#     st.markdown('#### Top States')
    
    

# st.divider()

st.divider()
#-------------------


