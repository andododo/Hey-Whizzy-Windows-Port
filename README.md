# Setup Guide

## In the /raspi folder:
For creating new UI:
```shell
npx create-react-app ui
```

```shell
npm install
npm install axios
npm install socket.io-client
```

## NPM troubleshooting
Delete node_modules if something went wrong.

A README file will be created on how to use the React, please check.
TL: use `npm start` on the frontend folder using cli

Make sure `pip` is installed and updated.
```shell
pip install --upgrade pip
```

## Prerequisites
```shell
pip install wheel
pip install --upgrade wheel
pip install setuptools
pip install --upgrade setuptools
```
Also, install C++ [Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

## Libraries for the project
```shell
pip install sounddevice
pip install SpeechRecognition
pip install simpleaudio
pip install pyttsx3
pip install lxml
pip install pygame
pip install flask-socketio
pip install Flask-MySQLdb
pip install python-dotenv
pip install PyAudio

```

## Gemini API Key
Get  your API key here: https://aistudio.google.com/app/apikey
For more information: https://ai.google.dev/


## Get IPv4 Address
```shell
ipconfig /all
```
Find the '(Preferred)'
