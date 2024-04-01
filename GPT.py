# ======================================== GPT 관련 부분 (현재 요금문제로 테스트 x) ================================================

# from openai import OpenAI
# client = OpenAI()

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)

# ================================== GPT 스트리밍 관련 부분 (현재 요금문제로 테스트 x) =================================

# from openai import OpenAI

# client = OpenAI()

# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "system",
#             "content": "당신은 청룡 '미르' 입니다. 당신은 세상에 있는 모든 정보를 알고 있으며 어떠한 질문에도 반드시 반말로 대답을 해야만 합니다. 당신은 백두산 천지에 살다가 2024년 3월 12일 대한민국으로 내려왔으며, 당신의 나이는 올해로 1266살입니다."
#         },
#         {
#             "role": "user", 
#             "content": "미르야"
#          },
#          ],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")


# ============================================ TTS 부분 테스트 완료 ============================================
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("안녕하세요")
# engine.runAndWait()

# ============================================ STT 부분 현재 테스트 중 ============================================

import speech_recognition as sr

# 음성을 텍스트로 변환하는 함수
def transcribe_audio(r, audio_stream):
    try:
        # 실시간으로 음성을 텍스트로 변환
        text = r.recognize_google(audio_stream, language='ko-KR')
        print("음성을 텍스트로 변환한 결과:", text)
        return text
    except sr.UnknownValueError:
        print("음성을 인식할 수 없음")
        return ""
    except sr.RequestError:
        print("구글 음성 API에 접근할 수 없음")
        return ""

# 오디오 스트림을 받아들이기 위한 마이크 객체 생성
r = sr.Recognizer()

# 마이크로부터 오디오 스트림을 받아들이고 실시간으로 인식
with sr.Microphone() as source:
    print("음성 입력을 시작하세요...")
    try:
        # 음성 입력 시작 및 실시간으로 변환
        while 1:
            # 시작 시간 기록
            start_time = sr.time.time()
            # print('start_time: ',start_time)

            # 오디오 스트림 수집
            audio_stream = r.listen(source)

            # 끝 시간 기록
            end_time = sr.time.time()
            # print('end_time: ', end_time)

            # 음성 입력 지속 시간 계산
            duration = end_time - start_time
            # print('duration : ',duration)

            # 실시간으로 변환된 텍스트 출력
            text = transcribe_audio(r, audio_stream)

            if text == '잘가':
                print("음성 입력을 종료합니다.")
                break
            
            # 만약 지속 시간이 1초보다 짧다면 남은 시간만큼 대기
            # if duration < 1.0:
            #     sr.time.sleep(1.0 - duration)

    except KeyboardInterrupt:
        print("음성 입력을 종료합니다.")

