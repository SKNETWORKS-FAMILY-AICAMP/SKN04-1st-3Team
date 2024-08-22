import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

st.header('자동차 등록대수')
st.divider()
#-------------------

st.subheader('시도 별 자동차 등록대수')
latitude = 37.394946
longitude = 127.111104


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
