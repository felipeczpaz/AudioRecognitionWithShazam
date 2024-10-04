import asyncio
import pyaudio
import wave
import time
from shazamio import Shazam

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2048
RECORD_SECONDS = 10

async def recognize_audio(audio_file):
    shazam = Shazam()
    out = await shazam.recognize(audio_file)
    if 'track' in out:
        song = out['track']
        print(f"Title: {song['title']}")
        print(f"Artist: {song['subtitle']}")
        print(f"Album: {song.get('sections', [{}])[0].get('metadata', [{}])[0].get('text', 'N/A')}")
        print(f"Shazam Link: {song['url']}")
    else:
        print("No song recognized or response format has changed.")
        print("Response:", out)

def list_audio_devices():
    p = pyaudio.PyAudio()
    devices = []
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        devices.append((i, info['name'], info['maxInputChannels']))
        print(f"Device {i}: {info['name']}, Channels: {info['maxInputChannels']}")
    p.terminate()
    return devices

def select_input_device(devices):
    while True:
        try:
            device_index = int(input("Select an input device by index: "))
            if device_index < 0 or device_index >= len(devices):
                print("Invalid index. Please try again.")
            else:
                return device_index
        except ValueError:
            print("Please enter a valid number.")

def record_audio(input_device_index):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=input_device_index,
                    frames_per_buffer=CHUNK)

    print(f"Recording audio for {RECORD_SECONDS} seconds...")
    audio_buffer = []

    start_time = time.time()
    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        audio_buffer.append(data)
        if time.time() - start_time > RECORD_SECONDS:
            print("Recording stopped after specified duration.")
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_data = b''.join(audio_buffer)

    with wave.open("temp_audio.wav", "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(audio_data)

    asyncio.run(recognize_audio("temp_audio.wav"))

if __name__ == "__main__":
    devices = list_audio_devices()
    input_device_index = select_input_device(devices)
    record_audio(input_device_index)
