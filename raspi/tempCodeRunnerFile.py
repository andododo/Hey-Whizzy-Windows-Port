import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sound_dir1 = r"\sounds\granted.wav"
sound_dir2 = r"\sounds\beep_down.wav"
file_path1 = os.path.join(os.path.dirname(current_dir), sound_dir1)
file_path2 = os.path.join(os.path.dirname(current_dir), sound_dir2)

print(file_path1)