import pyttsx3
import subprocess
import sounddevice as sd
import soundfile as sf
import requests

# Gets the directory of the script
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

def start_speaking(output):
    # Change the command to create output.wav
    piper_dir = r".\piper\piper.exe"
    command = f"echo '{output}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"

    # Change the current working directory
    cwd = os.path.join(os.path.dirname(current_dir), 'piper')

    # Run the command
    subprocess.run(command, shell=True, cwd=cwd)

    # Send the reply to the backend UI
    requests.post('http://localhost:5000/reply', json={'reply': output})

    # Play the output.wav file
    data, samplerate = sf.read(f"{cwd}/output.wav")
    sd.play(data, samplerate)
    print("audio played")
    sd.wait()  # Wait until the audio is finished playing
    print("audio finished")

    # Send a message to the frontend to stop the talking animation
    requests.post('http://localhost:5000/stop_talking')

def start_speaking_small(output, image_data):
    # Change the command to create output.wav
    piper_dir = r".\piper\piper.exe"
    command = f"echo '{output}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"

    # Change the current working directory
    cwd = os.path.join(os.path.dirname(current_dir), 'piper')

    # Run the command
    subprocess.run(command, shell=True, cwd=cwd)

    # Send the reply to the backend UI
    requests.post('http://localhost:5000/reply', json={'reply': output})
    requests.post('http://localhost:5000/image_data', json={'image_data': image_data})

    # Play the output.wav file
    data, samplerate = sf.read(f"{cwd}/output.wav")
    sd.play(data, samplerate)
    print("audio played")
    sd.wait()  # Wait until the audio is finished playing
    print("audio finished")

    # Send a message to the frontend to stop the talking animation
    requests.post('http://localhost:5000/stop_talking')

def start_speaking_large(output):
    print("working for reply large")

    # Change the command to create output.wav
    piper_dir = r".\piper\piper.exe"
    command = f"echo '{output}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"
    print(command)
    # Change the current working directory
    cwd = os.path.join(os.path.dirname(current_dir), 'piper')
    
    # Run the command
    subprocess.run(command, shell=True, cwd=cwd)

    # Send the reply to the backend UI
    requests.post('http://localhost:5000/reply_large', json={'reply': output})

    # Play the output.wav file
    data, samplerate = sf.read(f"{cwd}/output.wav")
    sd.play(data, samplerate)
    print("audio played")
    sd.wait()  # Wait until the audio is finished playing
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