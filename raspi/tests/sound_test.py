import pyaudio
import wave
import os

def play_wav_file():
    try:
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # file_path = os.path.join(os.path.dirname(current_dir), 'sounds', 'beep_down.wav')
        file_path = 'raspi/sounds/beep_down.wav' # need to implement better file locator here
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

play_wav_file()
