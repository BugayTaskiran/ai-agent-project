import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    print("API key is not found.")
    exit()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=google_api_key
)

prompt = ChatPromptTemplate(
    [
        ("system", "Sen teknik konuları anlatan bir eğitim asistanısın."),
        ("human", "Konu: {topic}"),
    ]
)

message = prompt.format_messages(
    topic="Büyük dil modelleri nelerdir?"
)

response = model.invoke(message)

print(response.content)