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

async def listen_and_transcribe():
    r = sr.Recognizer() # 오디오 스트림을 받아들이기 위한 마이크 객체 생성
    with sr.Microphone() as source:# 마이크로부터 오디오 스트림을 받아들이고 실시간으로 인식
        print("음성 입력을 시작하세요...")
        a=0
        while 1:
            audio_stream = r.listen(source)
            text = await transcribe_audio(r, audio_stream)# 실시간으로 변환된 텍스트 출력
            print(a,text)
            a=a+1
            if '잘가' in text:
                print("음성 입력을 종료합니다.")
                break

loop = asyncio.get_event_loop()
loop.run_until_complete(listen_and_transcribe())
loop.close()