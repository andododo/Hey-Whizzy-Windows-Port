import speech_recognition as sr
import requests
import pyaudio
import wave

def play_wav_file():
    print("test 1")
    try:
        file_path = 'sounds/beep_down.wav' # need to implement better file locator here
        wave_obj = wave.open(file_path, 'rb')
        play_obj = pyaudio.PyAudio()

        stream = play_obj.open(format=play_obj.get_format_from_width(wave_obj.getsampwidth()),
                        channels=wave_obj.getnchannels(),
                        rate=wave_obj.getframerate(),
                        output=True)
        
        chunk = 1024
        data = wave_obj.readframes(chunk)

        while data:
            stream.write(data)
            data =wave_obj.readframes(chunk)

        stream.stop_stream()
        stream.close()
        play_obj.terminate()

    except Exception as e:
        print(e)

def listen(mic_index):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=mic_index)

    wake_word_list = [
        "hey wheezy",
        "hey weezy",
        "hey weezy.",
        "hey, weezy",
        "hey, weezy.",   
        "hey weezy hey weezy",
        "hey wizzy",
        "hey wizzy hey wizzy",
        "play weezy",
        "play weezy play weezy",
        "hey easy",
        "hey rese",
        "abc",
        "a b c",
        "play music",
        "hey busy"
    ]

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("check 0")

        try:
            print("[1]Listening for wake word...")
            requests.post('http://localhost:5000/idle')
            audio = recognizer.listen(source, timeout=5)
            requests.post('http://localhost:5000/idle_stop')
            print("check 1")
            #initialize.update_label("Recognizing",30)
            # model_path = "/home/whizzy/my_project_venv/Hey-Whizzy-main/raspi/raspi_python/model"
            text = recognizer.recognize_google(audio)
            # result = recognize_vosk_custom(audio, model_path=model_path)
            # text = result["text"]
            print("check 2")
            play_wav_file()
            print(f"You said: {text.lower().strip()}")

            if text.lower().strip() in wake_word_list:
                print("Wake word detected! Initiating speech recognition...")
                requests.post('http://localhost:5000/change_background', json={'index': 2})
                return True
            else:
                print("Not wake word...")
        except sr.WaitTimeoutError:
            print("No audio detected within the timeout period")
            #subprocess.Popen(["python", "initialize.py"])
            #sys.exit(0)  # Terminate the process
            return False
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error connecting to the recognizer: {e}")

    return False