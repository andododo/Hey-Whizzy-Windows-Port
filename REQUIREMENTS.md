# Dev requirements

## In the /raspi folder:
```shell
npx create-react-app ui
npm install axios
npm install socket.io-client
```

A README file will be created on how to use the React, please check.
TL: use `npm start` on the frontend folder using cli

Make sure `pip` is installed and updated.
```shell
pip install --upgrade pip
```

Prerequisites
```shell
pip install wheel
pip install --upgrade wheel
pip install setuptools
pip install --upgrade setuptools
```
Also, install C++ [Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

Libraries for the project
```shell
pip install sounddevice
pip install SpeechRecognition
pip install simpleaudio
pip install pyttsx3
pip install lxml
pip install pygame
pip install flask-socketio
pip install Flask-MySQLdb
pip install PyAudio
pip install python-dotenv
```

Installing Piper TTS
1. Get zip file for Windows (amd64). https://github.com/rhasspy/piper/releases/tag/2023.11.14-2
2. In `main` folder (that would be: Hey_Whizzy-Windows-Port), create a folder named `piper`.
3. Move downloaded zip file there, and then 'extract here'.
4. Download the [voice model](https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/joe/medium/en_US-joe-medium.onnx?download=true) and the [json file](https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/joe/medium/en_US-joe-medium.onnx.json).

- https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/joe/medium/en_US-joe-medium.onnx?download=true
- https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/joe/medium/en_US-joe-medium.onnx.json

Notes:
1. The project uses `en_US-joe-medium`
2. Ctrl + S on the .json file to save it because there is download button for this. Reminder on the piper execution, you need the script to be /piper/piper.

