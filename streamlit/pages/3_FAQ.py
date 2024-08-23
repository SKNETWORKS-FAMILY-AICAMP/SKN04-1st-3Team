import streamlit as st

conn = st.connection('postgresql', type='sql')

st.title("QnA")
st.divider()

query = "SELECT Question, Answer FROM FAQ"
qna_df = conn.query(query, ttl=600)

qna_list = [(row['Question'], row['Answer']) for _, row in qna_df.iterrows()]

tabs = st.tabs([f"{i+1}page" for i in range((len(qna_list) + 4) // 5)])

def qna_container(q, a):
    with st.expander(q):
        st.write(a)

qna_chunks = [qna_list[i:i + 5] for i in range(0, len(qna_list), 5)]

for i, tab in enumerate(tabs):
    with tab:
        if i < len(qna_chunks):
            for qna in qna_chunks[i]:
                qna_container(qna[0], qna[1])
