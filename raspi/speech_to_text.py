import speech_recognition as sr
import requests
import pyaudio
import wave

def play_wav_file(type):
    try:
        file_path1 = r'raspi\sounds\granted.wav'
        file_path2 = r'raspi\sounds\beep_down.wav'
        
        if type == 1:
            wave_obj = wave.open(file_path1, 'rb')
        elif type == 2:
            wave_obj = wave.open(file_path2, 'rb')
        
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