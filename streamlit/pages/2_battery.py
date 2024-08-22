import streamlit as st
import pandas as pd
import numpy as np

# battery_producer()

st.title("배터리제조사 ")

select_brand = st.selectbox(
    '확인하고 싶은 브랜드를 선택해주세요.',
    ['현대자동차 및 제네시스','기아자동차','KG모빌리티', '르노', 'BMW', '벤츠', '아우디', '폭스바겐', '볼보', '스텔란티스(Jeep, 푸조, DS)', 
     '폴스타', '포르쉐', '토요타(렉서스)', '쉐보레', '재규어', '미니(BMW)', '롤스로이스', '지엠']
)
st.divider()

df = pd.DataFrame(
    np.random.randn(10, 2), columns=("차종", "제조사")
)

st.table(df)

#tmp_df = df[df['brand']== select_brand]