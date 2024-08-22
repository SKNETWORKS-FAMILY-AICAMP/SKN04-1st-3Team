import streamlit as st

st.title("QnA")
st.divider()

qna_list = [
    ("질문1", "답변1"),
    ("질문2", "답변2"),
    ("질문3", "답변3"),
    ("질문4", "답변4"),
    ("질문5", "답변5"),
    ("질문6", "답변6"),
    ("질문7", "답변7"),
    ("질문8", "답변8"),
    ("질문9", "답변9"),
    ("질문10", "답변10"),
    ("질문11", "답변11"),
    ("질문12", "답변12"),
    ("질문13", "답변13"),
    ("질문14", "답변14"),
    ("질문15", "답변15"),
]

tabs = st.tabs([f"{i+1}page" for i in range(3)])

def qna_container(q, a):
    with st.expander(q):
        st.write(a)

qna_chunks = [qna_list[i:i + 5] for i in range(0, len(qna_list), 5)]

for i, tab in enumerate(tabs):
    with tab:
        for qna in qna_chunks[i]:
            qna_container(qna[0], qna[1])
