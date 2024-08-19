import speech_recognition as sr
import time
import googlesearch
t=time.localtime()
def get_voice_text():
    r = sr.Recognizer()
    with sr.Microphone() as audio:
        text=None
        print("I : How can I help you")
        audio_text = r.listen(audio)
        try:
            text=r.recognize_google(audio_text)
            print("You :",text)
        except:
            print("I:Sorry, incovineance")
    return text
while True:
    text=get_voice_text()
    
    if text:
        text=text.lower()
        match(text):
            case('hello'):
                print('I : Helow! How can I help you ?')
            case('what is the time'):
                print('I : The time is',t.tm_hour,":",t.tm_min,':',t.tm_sec)
            case('what is the date'):
                print('I : The date is',t.tm_mday,'/',t.tm_mon,'/',t.tm_year)
            case('exit'):
                break
            case(text):
                query = str(text)
                for a in googlesearch.search(query,num=1,stop=1):
                    print("I : go through this link:",a)