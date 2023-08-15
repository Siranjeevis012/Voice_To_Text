from google.cloud import speech_v1p1beta1 as speech
import io

def transcribe_audio(audio_file_path, language_code="en-US"):
    client = speech.SpeechClient()

    with io.open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )

    response = client.recognize(config=config, audio=audio)

    transcribed_text = ""
    for result in response.results:
        transcribed_text += result.alternatives[0].transcript.strip() + " "

    return transcribed_text

if __name__ == "__main__":
    audio_file_path = "path/to/your/audio_file.wav"  # Replace with your audio file path
    text = transcribe_audio(audio_file_path)
    print("Transcribed Text:")
    print(text)
