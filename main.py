from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import streamlit as st
import pandas as pd

load_dotenv()

# llm = OpenAI()
# result = llm.predict("요즘 인기있는 일본 애니메이션은?")
# print(result)

chat_model = ChatOpenAI()
result = chat_model.predict("안녕하세요")
print(result)

st.title('인공지능 작사가')
content = st.text_input('노래의 주제를 제시해주세요:')
st.write("노래의 주제는", content)
if st.button("시 작성 요청하기"):
    result = chat_model.predict(content + "에 대한 노래 가사를 써줘.")
    st.write(result)
    

