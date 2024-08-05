# Default will be Google Speech Recognition API for language model
# Uncomment lines below if vosk is needed for language model
# from vosk import KaldiRecognizer, Model, SetLogLevel
# Set the log level to suppress the Vosk log messages

# SetLogLevel(-1)

# def recognize_vosk_custom(audio_data, language='en', model_path=None):
#     if model_path is None:
#         model_path = "model"
#     if not os.path.exists(model_path):
#         return f"Please download the model and provide the path to the 'model' folder."
#         exit(1)
    
#     model = Model(model_path)
#     rec = KaldiRecognizer(model, 16000)
    
#     rec.AcceptWaveform(audio_data.get_raw_data(convert_rate=16000, convert_width=2))
#     finalRecognition = rec.FinalResult()
    
#     return json.loads(finalRecognition)