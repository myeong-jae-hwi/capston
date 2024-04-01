import speech_recognition as sr


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

# 오디오 스트림을 받아들이기 위한 마이크 객체 생성
r = sr.Recognizer()
# 마이크로부터 오디오 스트림을 받아들이고 실시간으로 인식
with sr.Microphone() as source:
    print("음성 입력을 시작하세요...")

    try:
        # 음성 입력 시작 및 실시간으로 변환
        while 1:
            
            start_time = sr.time.time()# 시작 시간 기록
            audio_stream = r.listen(source)# 오디오 스트림 수집
            print(audio_stream)
            end_time = sr.time.time()# 끝 시간 기록
            duration = end_time - start_time # 음성 입력 지속 시간 계산
            print(start_time)
            print(end_time)
            print(duration)
            if duration < 0.5:# 만약 지속 시간이 1초보다 짧다면 남은 시간만큼 대기
                sr.time.sleep(0.5 - duration)

            text = transcribe_audio(r, audio_stream)# 실시간으로 변환된 텍스트 출력
            print(text)
            if '잘가' in text:
                print("음성 입력을 종료합니다.")
                break          
    except KeyboardInterrupt:
        print("음성 입력을 종료합니다.")