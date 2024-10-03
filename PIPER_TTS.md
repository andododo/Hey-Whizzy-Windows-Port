# Installing Piper TTS 

Only need to do this if you need to download it again. Piper is already part of the source code when cloned.

1. Get zip file for Windows (amd64). https://github.com/rhasspy/piper/releases/tag/2023.11.14-2
2. In `main` folder (that would be: Hey_Whizzy-Windows-Port), create a folder named `piper`.
3. Move downloaded zip file there, and then 'extract here'.
4. Download the [voice model](https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/joe/medium/en_US-joe-medium.onnx?download=true) and the [json file](https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/joe/medium/en_US-joe-medium.onnx.json).

- https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/joe/medium/en_US-joe-medium.onnx?download=true
- https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/joe/medium/en_US-joe-medium.onnx.json

Notes:
1. The project uses `en_US-joe-medium`
2. Ctrl + S on the .json file to save it because there is download button for this. Reminder on the piper execution, you need the script to be /piper/piper.

