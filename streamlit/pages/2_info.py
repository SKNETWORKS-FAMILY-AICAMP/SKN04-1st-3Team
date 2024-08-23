import streamlit as st

conn = st.connection('postgresql', type='sql')

st.title('내 자동차 배터리 제조사는?')

select_brand = st.selectbox(
    '확인하고 싶은 브랜드를 선택해주세요.',
    ['현대자동차 및 제네시스', '기아자동차', 'KG모빌리티', '르노', 'BMW', '벤츠', '아우디', '폭스바겐', '볼보', '스텔란티스(Jeep, 푸조, DS)', 
     '폴스타', '포르쉐', '토요타(렉서스)', '쉐보레', '재규어', '미니(BMW)', '롤스로이스', '지엠']
)

st.divider()

query = "SELECT car, battery FROM battery"

df = conn.query(query, ttl=600)

if df.empty:
    st.write("배터리 정보가 없습니다.")
else:
    st.table(df.rename(columns={'car': '차종', 'battery': '제조사'}))
