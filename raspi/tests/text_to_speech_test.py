import os
import subprocess
import pyaudio
import wave
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))
cwd = os.path.join(os.path.dirname(current_dir), 'piper')
model_name = "en_US-joe-medium.onnx"
piper_dir = r".\piper\piper.exe"

def generate_audio(text):
    output_file = os.path.join(cwd, 'output.wav')
    command = f"echo '{text}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"
    subprocess.run(command, shell=True, cwd=cwd)
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

def start_speaking(text, reply_type=0, image_data=None):
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
    start_speaking("Sorry, I didn't quite hear you well.")

def set_reply(output, reply_type, image_data):
    start_speaking(output, reply_type, image_data)

# Example usage
# if __name__ == "__main__":
#     start_speaking("Hello, this is a test message.")
#     no_pick_up()
#     set_reply("This is a small reply with image data", 2, "image_data_here")
#     set_reply("This is a large reply", 1)


# ORIGINAL BELOW

# import pyttsx3
# import subprocess
# import simpleaudio
# import requests

# # Gets the dicrectory of the script
# import os
# current_dir = os.path.dirname(os.path.abspath(__file__))

# def start_speaking(output):
#     # Change the command to create output.wav
#     piper_dir = r".\piper\piper.exe"
#     command = f"echo '{output}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"

#     # Change the current working directory
#     cwd = os.path.join(os.path.dirname(current_dir), 'piper')

#     # Run the command
#     subprocess.run(command, shell=True, cwd=cwd)

#     # Play the output.wav file
#     wave_obj = simpleaudio.WaveObject.from_wave_file(f"{cwd}/output.wav")
#     play_obj = wave_obj.play()
#     print("audio played")

#     # Send the reply to the backend UI
#     requests.post('http://localhost:5000/reply', json={'reply': output})

#     # Wait for the audio to finish playing
#     play_obj.wait_done()
#     print("audio finished")

#     # Send a message to the frontend to stop the talking animation
#     requests.post('http://localhost:5000/stop_talking')

# def start_speaking_small(output, image_data):
#     # Change the command to create output.wav
#     piper_dir = r".\piper\piper.exe"
#     command = f"echo '{output}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"

#     # Change the current working directory
#     cwd = os.path.join(os.path.dirname(current_dir), 'piper')

#     # Run the command
#     subprocess.run(command, shell=True, cwd=cwd)

#     # Play the output.wav file
#     wave_obj = simpleaudio.WaveObject.from_wave_file(f"{cwd}/output.wav")
#     play_obj = wave_obj.play()
#     print("audio played")

#     # Send the reply to the backend UI
#     requests.post('http://localhost:5000/reply', json={'reply': output})
#     requests.post('http://localhost:5000/image_data', json={'image_data': image_data})

#     # Wait for the audio to finish playing
#     play_obj.wait_done()
#     print("audio finished")

#     # Send a message to the frontend to stop the talking animation
#     requests.post('http://localhost:5000/stop_talking')

# def start_speaking_large(output):
#     print("working for reply large")

#     # Change the command to create output.wav
#     piper_dir = r".\piper\piper.exe"
#     command = f"echo '{output}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"

#     # Change the current working directory
#     cwd = os.path.join(os.path.dirname(current_dir), 'piper')
    
#     # Run the command
#     subprocess.run(command, shell=True, cwd=cwd)

#     # Play the output.wav file
#     wave_obj = simpleaudio.WaveObject.from_wave_file(f"{cwd}/output.wav")
#     play_obj = wave_obj.play()
#     print("audio played")

#     # Send the reply to the backend UI
#     requests.post('http://localhost:5000/reply_large', json={'reply': output})

#     # Wait for the audio to finish playing
#     play_obj.wait_done()
#     print("audio finished")

#     # Send a message to the frontend to stop the talking animation
#     requests.post('http://localhost:5000/stop_talking')

# def no_pick_up():
#     reply = "Sorry, I didn't quite hear you well."
#     start_speaking(reply)

# def set_reply(output, reply_type, image_data):
#     if reply_type == 1:
#         start_speaking_large(output)
#     elif reply_type == 2:
#         start_speaking_small(output, image_data)