import speech_recognition as sr

# 음성 파일 로드
# r = sr.Recognizer()
# with sr.AudioFile('hi.wav') as source:
#     audio = r.record(source)

# # 음성을 텍스트로 변환
# try:
#     text = r.recognize_google(audio, language='ko-KR')
#     print("음성을 텍스트로 변환한 결과:", text)
# except sr.UnknownValueError:
#     print("음성을 인식할 수 없음")
# except sr.RequestError:
#     print("구글 음성 API에 접근할 수 없음")

filename="hi.wav"
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text=r.recognize_google(audio_data, language='ko-KR')
    print(text)