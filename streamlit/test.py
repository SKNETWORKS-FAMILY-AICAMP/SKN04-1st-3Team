import streamlit as st
import pandas as pd
import folium
import json
from streamlit_folium import st_folium
import altair as alt

# 스타일 및 페이지 설정
st.set_page_config(page_title="자동차 등록대수 현황", page_icon="🚗", layout="wide")

# 데이터 로드 및 설정
geo_path = 'SIDO_MAP.json'
with open(geo_path, encoding='utf-8') as f:
    geo_data = json.load(f)

# 데이터 프레임 설정
# 예시 데이터, 실제 데이터 구조에 맞게 조정해야 합니다.
# 지역 목록
regions = ['서울특별시', '경기도', '인천광역시', '부산광역시', '대구광역시', '대전광역시', '광주광역시', '울산광역시', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
# 연도 범위
years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

# 데이터 생성: 각 연도와 지역별로 값 생성
data = {
    'year': [year for year in years for _ in range(len(regions))],  # 연도 반복
    'region': regions * len(years),  # 지역 반복
    'value': [i + j * 1000 for j in range(len(years)) for i in range(10000, 10000 + 1000 * len(regions), 1000)]  # 값 생성
}

# 데이터 프레임 생성
df = pd.DataFrame(data)

# 슬라이더를 메인 콘텐츠에 배치
year_list = list(df['year'].unique())
selected_year = st.slider('Select a year', min_value=min(year_list), max_value=max(year_list), value=max(year_list))
df_selected_year = df[df['year'] == selected_year]
df_selected_year_sorted = df_selected_year.sort_values(by="value", ascending=False)

# Streamlit에서 2개의 컬럼 생성
col = st.columns((0.8, 0.2), gap='medium')

# 지도 그리기
with col[0]:
    st.subheader('시도 별 자동차 등록대수')
    m = folium.Map(location=[36.2, 127.5], zoom_start=7, control_scale=True)
    color_scale = folium.LinearColormap(colors=['#FFEDA0', '#FEB24C', '#F03B20'], vmin=df_selected_year['value'].min(), vmax=df_selected_year['value'].max())
    folium.GeoJson(
        geo_data,
        style_function=lambda feature: {
            'fillColor': color_scale(df_selected_year[df_selected_year['region'] == feature['properties']['CTP_KOR_NM']]['value'].iloc[0] if not df_selected_year[df_selected_year['region'] == feature['properties']['CTP_KOR_NM']].empty else 0),
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.7
        },
        tooltip=folium.features.GeoJsonTooltip(fields=['CTP_KOR_NM'], aliases=['Region:'], localize=True)
    ).add_to(m)
    st_folium(m, width=700, height=500)

# 도넛 차트 및 데이터 표시
with col[1]:
    st.markdown('#### Top States')
    st.dataframe(df_selected_year_sorted.head(5), width=300)  # Top 5 지역만 표시
    st.subheader('도넛 차트')
    # 도넛 차트 추가 예시
    response_value = 75  # 임시 값, 실제 데이터로 변경 필요
    selected_color_theme = 'blues'  # 색상 테마 선택
    st.altair_chart(make_donut(response_value, 'Electric Vehicles', selected_color_theme), use_container_width=True)

    with st.expander('About', expanded=True):
        st.write('''
            - Data: [Korea Vehicle Registration Data](https://example.com).
            - Gains/Losses: Year-over-year change.
            - Threshold: Values > 50,000 are highlighted.
            ''')

st.divider()
