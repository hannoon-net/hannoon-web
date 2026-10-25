import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# prompt.txt 읽기
with open("prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

# 제미나이 호출
client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt
)

# 결과 저장
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("완료! result.txt를 확인하세요.")