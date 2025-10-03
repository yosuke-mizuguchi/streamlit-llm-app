
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# Streamlit UI

st.title("LLM専門家デモ")
st.markdown("""
### アプリ概要
このWebアプリは、LLM（大規模言語モデル）に専門家として振る舞わせることができるデモです。下記の手順でご利用ください。

#### 操作方法
1. 「専門家の種類を選択してください」から、地理の専門家または料理の専門家を選択します。
2. 質問したい内容を「質問を入力してください」に入力します。
3. 「送信」ボタンを押すと、選択した専門家としてLLMが回答します。
""")

expert_type = st.radio(
    "専門家の種類を選択してください:",
    ("A: 地理の専門家", "B: 料理の専門家")
)

user_input = st.text_input("質問を入力してください", "")


def get_llm_response(input_text: str, expert_type: str) -> str:
    """
    入力テキストと専門家の種類を受け取り、LLMの回答を返す関数
    """
    if expert_type.startswith("A"):
        system_prompt = "あなたは地理の専門家です。地理に関する質問には専門的かつ分かりやすく答えてください。"
    elif expert_type.startswith("B"):
        system_prompt = "あなたは料理の専門家です。料理に関する質問には専門的かつ分かりやすく答えてください。"
    else:
        system_prompt = "あなたは親切なアシスタントです。"

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=input_text),
    ]
    result = llm(messages)
    return result.content

if st.button("送信"):
    response = get_llm_response(user_input, expert_type)
    st.write(response)
