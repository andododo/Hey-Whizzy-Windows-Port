# module imports
import wake_word
import speech_to_text
import conversation_gemini
import text_to_speech
import get_prompt
import fetch_request
# import sounddevice
import time
import requests

# 1. Provide more instructions and reinforcement
# Please wait for my reply!
# Choose which mode
# Thank you!
# Please use English!

def start():
    # Specify the microphone index (use microphone_list.py)
    # index 1 is usually the primary device used
    mic_index = 1  # Change this to the mic to use
    
    requests.post('http://localhost:5000/change_background', json={'index': 1})

    # Step 1 - wake word
    # Keep listening until the wake word is detected
    bool_wake = False
    bool_wake = wake_word.listen(mic_index)

    if bool_wake:
        # Step 2 - whizzy's initial response
        prompt_type = get_prompt.main_func(mic_index)
        # Step 3
        if prompt_type == 1:
            # Step 3a -  get answer from db
            command = speech_to_text.recognize_speech(mic_index)
            if command is not None:
                output, reply_type, image_data = fetch_request.post_command(command)
                if reply_type == 1:
                    requests.post('http://localhost:5000/change_background', json={'index': 6}) 
                elif reply_type == 2:
                    requests.post('http://localhost:5000/change_background', json={'index': 1}) 
                text_to_speech.set_reply(output, reply_type, image_data)
                time.sleep(5)
            else:
                text_to_speech.no_pick_up()
        elif prompt_type == 2:
            # Step 3b.1 - speech-to-text
            command = speech_to_text.recognize_speech(mic_index)
            # Step 3b.2 - send input to gemini
            if command is not None:
                output = conversation_gemini.start_prompt(command)
                requests.post('http://localhost:5000/change_background', json={'index': 6}) 
                # Step 3b.3 - geminip output to text-to-speech
                text_to_speech.start_speaking_large(output)
                time.sleep(5)
            else:
                text_to_speech.no_pick_up()

if __name__ == "__main__":
    
    while True:
        start()