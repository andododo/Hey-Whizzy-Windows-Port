import speech_recognition as sr
import requests
import sounddevice as sd
import soundfile as sf

def play_wav_file():
    file_path = 'sounds/beep_down.wav' # need to implement better file locator here
    
    # Play wav file
    data, samplerate = sf.read(file_path)
    buffer_size = 1024  # You can adjust this value
    sd.play(data, samplerate, blocksize=buffer_size)
    sd.wait()  # Wait until the audio is finished playing

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