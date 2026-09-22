import sounddevice as sd
from scipy.io.wavfile import write
import whisper

SAMPLE_RATE = 16000
DURATION = 5

print("Recording... speak now.")
audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
sd.wait()
print("Recording finished.")

write("recording.wav", SAMPLE_RATE, audio)

print("Loading Whisper model...")
model = whisper.load_model("base")

print("Transcribing...")
result = model.transcribe("recording.wav")

print("You said:", result["text"])