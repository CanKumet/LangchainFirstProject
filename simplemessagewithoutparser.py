from http.client import responses

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model = "gpt-4", temperature=0.1)
content1 = input("Bir metin giriniz: ")  # Kullanıcıdan string değer al

messages = [
    HumanMessage(content = "Translate the following from Turkish to English"),
    SystemMessage(content= content1)
    ]

parser = StrOutputParser()

chain = model | parser




if __name__ == "__main__":
    print(chain.invoke(messages))
