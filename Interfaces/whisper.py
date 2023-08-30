import whisper
import pyaudio
import wave
import numpy as np
from scipy.io import wavfile

class Audio:
    def __init__(self):
        self.e = 0

    def VoiceCommand(self):

        chunk = 1024
        sample_format = pyaudio.paInt16
        channels = 1
        fs = 44100
        seconds = 3.8
        filename = "audio.wav"
        threshold = 5000
        p = pyaudio.PyAudio()
        print('Listening')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []
        while True:
            data = stream.read(chunk)
            signal = np.frombuffer(data, dtype=np.int16)
            amplitude = np.max(signal)
            if amplitude > threshold:
                break

        try:
            notification_sound_file = 'Lily/speechdetected.mp3'
            play_sound_in_background(notification_sound_file)
        except:
            pass

        print('Recording')

        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        p.terminate()

        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

        ResponseOutput = self.speech()

        return ResponseOutput

    def speech(self):
        options = whisper.DecodingOptions(fp16 = False)

        self.model = whisper.load_model("base.en")
        rate, data = wavfile.read("audio.wav")

        result = self.model.transcribe("audio.wav")
        sentence = result["text"]

        print(sentence)

if __name__ == "__main__":
    VoiceInput = Audio()
    VoiceInput.VoiceCommand()
