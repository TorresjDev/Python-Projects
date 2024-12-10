import wave # Python library for reading and writing sound files
import numpy as np # Python library for numerical operations
import matplotlib.pyplot as plt # Python library for plotting data

# * Visualize Sound in Python

wav_obj = wave.open("../sounds/decibel-10s.wav", "rb") # rb mode returns a "read only" object

sample_freq = wav_obj.getframerate() # Sample frequency of the sound file in (Hz)
print(f"Sample frequency: {sample_freq} Hz")

total_samples = wav_obj.getnframes() # Total number of frames (samples) in the sound file
print(f"Number of samples: {total_samples}")

signal_duration = total_samples / sample_freq # Calculate the duration of the sound file in seconds
print(f"Duration of the sound file: {signal_duration} s")

num_audio_channel = wav_obj.getnchannels() # getnchannels() returns the number of audio channels in the sound file
print(f"Number of audio channels: {num_audio_channel}")

raw_signal_wave = wav_obj.readframes(total_samples) # readframes() reads the sound file and returns audio data object
# print(f"Audio data: {raw_signal_wave}")

signal_amplitude_array = np.frombuffer(raw_signal_wave, dtype=np.int16) # Convert the audio data to a numpy array as a 16-bit signed integer
print(f"Audio data as numpy array: {signal_amplitude_array}")

# Check for mono or stereo and handle accordingly
channel_type = "audio"
if num_audio_channel == 1:  # Mono audio
    print("Mono audio detected.")
    l_channel = signal_amplitude_array  # Use the full signal array
    r_channel = None  # No right channel for mono
    channel_type = "Mono Audio"
else:  # Stereo audio
    print("Stereo audio detected.")
    l_channel = signal_amplitude_array[0::2]  # Left channel
    r_channel = signal_amplitude_array[1::2]  # Right channel
    channel_type = "Stereo Audio"


# ! Plotting the Signal Amplitude
# before plotting the signal, we need to calculate the time at which each sample is taken
# time_value = np.linspace(0, total_samples / sample_freq, num=total_samples) # create an array of time values
time_value = np.linspace(0, signal_duration, num=total_samples) # create an array of time values
print(f"Time array: {time_value}")

plt.figure(figsize=(15, 5))
plt.plot(time_value, l_channel, label=f"Channel Type: {channel_type}", color="blue") # plot the left channel
plt.title(f"{channel_type} signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.xlim(0, signal_duration)
plt.legend()
plt.grid()
plt.show()

# ! Plotting the Frequency Spectrum
#   - Also known as spectrogram
#     - Its a visual representation of the signal strength at different frequencies
#     - It shows which frequencies are visible as a function of time

plt.figure(figsize=(15, 5))
plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50) # plot the spectrogram
plt.title(f"{channel_type} signal")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.ylim(0, 10000) # limit the frequency range
plt.xlim(0, signal_duration) # limit the time range
plt.colorbar(label="Intensity (dB)")
plt.show()

