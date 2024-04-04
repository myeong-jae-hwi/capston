import asyncio
import speech_recognition as sr

async def transcribe_audio(r, audio_stream):# 음성을 텍스트로 변환하는 함수
    try: # 실시간으로 음성을 텍스트로 변환
        text = r.recognize_google(audio_stream, language='ko-KR')
        return text
    except sr.UnknownValueError:
        return "음성을 인식할 수 없음"
    except sr.RequestError:
        return "구글 음성 API에 접근할 수 없음"

async def main():
    on_off=False #온오프 스위치, 마이크가 켜져있는데 사용자가 부르지 않으면 작동하지 않게하기 위해서 필요함
    r = sr.Recognizer() # 오디오 스트림을 받아들이기 위한 마이크 객체 생성
    with sr.Microphone() as source:# 마이크로부터 오디오 스트림을 받아들이고 실시간으로 인식
        while 1:
            audio_stream = r.listen(source)
            text = await transcribe_audio(r, audio_stream)# 실시간으로 변환된 텍스트 출력

            if '미르야'==text and on_off==False: #기기가 미작동일떄 미르를 부르면 작동.
                on_off=True

            if on_off==True: #기기가 작동중일때
                print(text)
                on_off==False #기기가 작동할떄 미작동상태로 만듬.

main()