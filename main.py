import speech_recognition as sr
import pyttsx3
from openai import OpenAI

engine = pyttsx3.init()
client = OpenAI()
on = False

# 음성을 텍스트로 변환하는 함수 
def transcribe_audio(r, audio_stream):
    try:
        # 실시간으로 음성을 텍스트로 변환
        text = r.recognize_google(audio_stream, language='ko-KR')
        return text
    except sr.UnknownValueError:
        return "음성을 인식할 수 없음"
    except sr.RequestError:
        return "구글 음성 API에 접근할 수 없음"

# GPT로부터 응답을 받는 함수
def get_gpt_response(user_input):
    # print(user_input)
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system","content": "당신은 청룡 '미르' 입니다. 당신은 세상에 있는 모든 정보를 알고 있으며 어떠한 질문에도 반드시 반말로 대답을 해야만 합니다. 당신은 백두산 천지에 살다가 2024년 3월 12일 대한민국으로 내려왔으며, 당신의 나이는 올해로 1266살입니다."},
            {"role": "user", "content": user_input},
        ]
    )
    print(stream.choices[0].message.content)
    return stream.choices[0].message.content


# 오디오 스트림을 받아들이기 위한 마이크 객체 생성
r = sr.Recognizer()

# 마이크로부터 오디오 스트림을 받아들이고 실시간으로 인식
with sr.Microphone() as source:
    print("음성 입력을 시작하세요...")

    while 1:
        try:
            start_time = sr.time.time()  # 시작 시간 기록
            audio_stream = r.listen(source, timeout=2)  # 오디오 스트림 수집
            end_time = sr.time.time()  # 끝 시간 기록
            duration = end_time - start_time  # 음성 입력 지속 시간 계산
            text = transcribe_audio(r, audio_stream)  # 실시간으로 변환된 텍스트 출력
            print(text, duration)

            # ============================== 미르의 전원 켜기 =====================================
            if '미르야' in text:
                print("미르 전원 ON (이 부분에 LED ON)")
                on = True

            if on:
                gpt_response = get_gpt_response(text)
                print("GPT:", gpt_response)
                engine.say(gpt_response)
                engine.runAndWait()

            if text == '잘가' and on:
                print("GPT 모드 해제")
                engine.say("GPT 모드가 해제되었습니다.")
                engine.runAndWait()
                on = False
                break
        except:
            print("time out")
        
    # except KeyboardInterrupt:
    #     print("음성 입력을 종료합니다.")
