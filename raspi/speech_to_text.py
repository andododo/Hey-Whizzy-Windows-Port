import speech_recognition as sr
import requests
import sounddevice as sd
import soundfile as sf

def play_wav_file(type):

    file_path1 = 'sounds/granted.wav'
    file_path2 = 'sounds/beep_down.wav'
    
    if type == 1:
        data, samplerate = sf.read(file_path1)
    elif type == 2:
        data, samplerate = sf.read(file_path2)
        
    # Play the audio
    buffer_size = 1024  # You can adjust this value
    sd.play(data, samplerate, blocksize=buffer_size)
    sd.wait()  # Wait until the audio is finished playing

def recognize_speech(mic_index):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=mic_index)

      
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("check 0")

        try:
            print("[2]Listening for audio...")
            play_wav_file(1)
            requests.post('http://localhost:5000/idle_stop')
            audio = recognizer.listen(source, timeout=5)
            print("check 1")
            # model_path = "/home/whizzy/my_project_venv/Hey-Whizzy-main/raspi/raspi_python/model"
            text = recognizer.recognize_google(audio)
            # result = recognize_vosk_custom(audio, model_path=model_path)
            # text = result["text"]
            print("check 2")
            play_wav_file(2)

            print(f"You said: {text.strip()}")
            return text.strip()
        
        except sr.WaitTimeoutError:
            err = "WaitTimeoutError"
            print("No audio detected within the timeout period")
            return err
        except sr.UnknownValueError as e:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Error connecting to Google Speech Recognition service: {e}")