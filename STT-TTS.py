import os
from dotenv import load_dotenv
import asyncio
import speech_recognition as sr
import pyttsx3
import openai as ai
from openai import OpenAI

async def transcribe_audio(r, audio_stream):# 음성을 텍스트로 변환하는 함수
    try: # 실시간으로 음성을 텍스트로 변환
        text = r.recognize_google(audio_stream, language='ko-KR')
        return text
    except sr.UnknownValueError:
        return "음성을 인식할 수 없음"
    except sr.RequestError:
        return "구글 음성 API에 접근할 수 없음"

# load_dotenv()
# api_key= os.getenv('open_ai_key')
# print(api_key)

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "당신은 청룡 '미르' 입니다. 당신은 세상에 있는 모든 정보를 알고 있으며 어떠한 질문에도 반드시 반말로 대답을 해야만 합니다. 당신은 백두산 천지에 살다가 2024년 3월 12일 대한민국으로 내려왔으며, 당신의 나이는 올해로 1266살입니다."
        },
        {
            "role": "user", 
            "content": "미르야"
         },
         ],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")


async def main():
    on_off=False #온오프 스위치, 마이크가 켜져있는데 사용자가 부르지 않으면 작동하지 않게하기 위해서 필요함
    r = sr.Recognizer() # 오디오 스트림을 받아들이기 위한 마이크 객체 생성
    with sr.Microphone() as source:# 마이크로부터 오디오 스트림을 받아들이고 실시간으로 인식
        while 1:
            audio_stream = r.listen(source)
            text = await transcribe_audio(r, audio_stream)# 실시간으로 변환된 텍스트 출력

            if '미르야'==text and on_off==False: #기기가 대기 중 미르를 부르면 작동.
                on_off=True #기기 작동

            if on_off==True: #기기가 작동 중일때
                print(text)
                engine.say(text)
                engine.runAndWait()
                on_off==False #기기 대기

engine = pyttsx3.init()
main()