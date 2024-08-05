import pyttsx3
import subprocess
import requests
import pyaudio
import wave

# Gets the directory of the script
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

def start_speaking(output):
    piper_dir = r".\piper\piper.exe"
    command = f"echo '{output}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"

    # Change the current working directory
    cwd = os.path.join(os.path.dirname(current_dir), 'piper')

    # Run the command
    subprocess.run(command, shell=True, cwd=cwd)

    # Send the reply to the backend UI
    requests.post('http://localhost:5000/reply', json={'reply': output})

    # Play output.wav file
    with wave.open(f"{cwd}/output.wav", 'rb') as wave_obj:
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
        print("audio played")

        stream.stop_stream()
        stream.close()
        play_obj.terminate()
        print("audio finished")

    # Send a message to the frontend to stop the talking animation
    requests.post('http://localhost:5000/stop_talking')

def start_speaking_small(output, image_data):
    piper_dir = r".\piper\piper.exe"
    command = f"echo '{output}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"

    # Change the current working directory
    cwd = os.path.join(os.path.dirname(current_dir), 'piper')

    # Run the command
    subprocess.run(command, shell=True, cwd=cwd)

    # Send the reply to the backend UI
    requests.post('http://localhost:5000/reply', json={'reply': output})
    requests.post('http://localhost:5000/image_data', json={'image_data': image_data})

    # Play output.wav file
    with wave.open(f"{cwd}/output.wav", 'rb') as wave_obj:
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
        print("audio played")

        stream.stop_stream()
        stream.close()
        play_obj.terminate()
        print("audio finished")

    # Send a message to the frontend to stop the talking animation
    requests.post('http://localhost:5000/stop_talking')

def start_speaking_large(output):
    print("inside for reply large")
    output = output.strip() # Removes new lines and spaces; usage is for shell command

    piper_dir = r".\piper\piper.exe"
    command = f"echo '{output}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"
    print(command)
    # Change the current working directory
    cwd = os.path.join(os.path.dirname(current_dir), 'piper')
    
    # Run the command
    subprocess.run(command, shell=True, cwd=cwd)

    # Send the reply to the backend UI
    requests.post('http://localhost:5000/reply_large', json={'reply': output})

    # Play output.wav file
    with wave.open(f"{cwd}/output.wav", 'rb') as wave_obj:
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
        print("audio played")

        stream.stop_stream()
        stream.close()
        play_obj.terminate()
        print("audio finished")

    # Send a message to the frontend to stop the talking animation
    requests.post('http://localhost:5000/stop_talking')

def no_pick_up():
    reply = "Sorry, I didn't quite hear you well."
    start_speaking(reply)

# This is for school-related answers
def set_reply(output, reply_type, image_data):
    if reply_type == 1:
        start_speaking_large(output)
    elif reply_type == 2:
        start_speaking_small(output, image_data)