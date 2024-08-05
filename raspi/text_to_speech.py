import os
import subprocess
import pyaudio
import wave
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
piper_dir = os.path.join(os.path.dirname(current_dir), 'piper')
piper_exe = os.path.join(piper_dir, 'piper.exe')
model_path = os.path.join(piper_dir, 'en_US-joe-medium.onnx')

def generate_audio(text):
    output_file = os.path.join(piper_dir, 'output.wav')
    command = f'echo "{text}" | "{piper_exe}" --model "{model_path}" --output_file "{output_file}"'
    subprocess.run(command, shell=True, cwd=piper_dir)
    return output_file

def play_audio(file_path):
    with wave.open(file_path, 'rb') as wave_obj:
        play_obj = pyaudio.PyAudio()
        stream = play_obj.open(format=play_obj.get_format_from_width(wave_obj.getsampwidth()),
                        channels=wave_obj.getnchannels(),
                        rate=wave_obj.getframerate(),
                        output=True)

        chunk_size = 1024
        data = wave_obj.readframes(chunk_size)

        while data:
            stream.write(data)
            data = wave_obj.readframes(chunk_size)

        stream.stop_stream()
        stream.close()
        play_obj.terminate()

def send_reply(reply, endpoint='reply'):
    requests.post(f'http://localhost:5000/{endpoint}', json={'reply': reply})

def send_image_data(image_data):
    requests.post('http://localhost:5000/image_data', json={'image_data': image_data})

def speak(text, reply_type=0, image_data=None):
    print("Generating and playing audio...")
    audio_file = generate_audio(text)
    
    if reply_type == 1:
        send_reply(text, 'reply_large')
    elif reply_type == 2:
        send_reply(text)
        if image_data:
            send_image_data(image_data)
    else:
        send_reply(text)

    play_audio(audio_file)
    print("Audio finished")

    requests.post('http://localhost:5000/stop_talking')

def no_pick_up():
    speak("Sorry, I didn't quite hear you well.")

def set_reply(output, reply_type, image_data):
    speak(output, reply_type, image_data)

# Example usage
# if __name__ == "__main__":
#     speak("Hello, this is a test message.")
#     no_pick_up()
#     set_reply("This is a small reply with image data", 2, "image_data_here")
#     set_reply("This is a large reply", 1)