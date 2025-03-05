from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv()

model = ChatOpenAI(model = "gpt-4", temperature=0.1)
content1 = input("Bir metin giriniz: ")  # Kullanıcıdan string değer al

messages = [
    HumanMessage(content = "Translate the following from Turkish to English"),
    SystemMessage(content= content1)
    ]


if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content)
