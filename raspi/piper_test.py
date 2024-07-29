import subprocess
import simpleaudio

# Gets the dicrectory of the script
import os
current_dir = os.path.dirname(os.path.abspath(__file__))


text = "This is a test using Piper TTS HAHAHA"

# Change the command to create output.wav
piper_dir = r".\piper\piper.exe"
command = f"echo '{text}' | {piper_dir} --model en_US-joe-medium.onnx --output_file output.wav"

# Change the current working directory
cwd = os.path.join(os.path.dirname(current_dir), 'piper')

# Use lines below if .dirname does not work
# base_dir = r"C:\Users\Ando\Documents\Hey-Whizzy-Windows-Port"
# cwd = os.path.join(base_dir, "piper")

# Run the command
subprocess.run(command, shell=True, cwd=cwd)

# Play the output.wav file
wave_obj = simpleaudio.WaveObject.from_wave_file(f"{cwd}/output.wav")
play_obj = wave_obj.play()

# Wait for the audio to finish playing
play_obj.wait_done()