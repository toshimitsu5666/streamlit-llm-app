from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

#LLM ChatPromptTemplate、関数定義
def llm_response(genre, question):
    # genre = selected_item
    # question = input_message

  system_template = "あなたは、{genre}の専門家です。質問に対して初心者にも分かりやすく簡潔に答えてください。"

  human_template = "{question}"

  prompt = ChatPromptTemplate.from_messages([
      SystemMessagePromptTemplate.from_template(system_template),
      HumanMessagePromptTemplate.from_template(human_template),
  ])

  messages = prompt.format_prompt(genre=genre, question=question).to_messages()

#messages

  from langchain_openai import ChatOpenAI

  llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

  try:
       result = llm.invoke(messages)
       return result.content
  except Exception as e:
       return f"エラーが発生しました:, {e}"

import streamlit as st

st.title("LLMアプリ")
st.write("##### 質問するジャンルを選択してください")
st.write("ジャンルを選択し、入力フォームに質問を入力し、「送信」ボタンを押してください。")

selected_item = st.radio(
    "質問するジャンルを選択してください。",
    ["健康", "スポーツ"]
)

genre = selected_item

input_message = st.text_input(label="質問を入力してください。")

question = input_message

if st.button("送信"):
    st.divider()

# genre ="スポーツ"
# question ="筋肉痛はどうすれば治りますか"

    response = llm_response(genre, question)
    st.write("##### 回答")
    st.write(response)
    st.balloons()
# print(response)
