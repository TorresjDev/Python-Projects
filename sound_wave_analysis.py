import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the WAV file (replace "sounds/radar.wav" with your actual file path)
sample_rate, data = wavfile.read("sounds/decibel-stps-x10.wav")

length = data.shape[0] / sample_rate
print(f"length = {length}s and the sample rate = {sample_rate}Hz and the data {data}")

# Select a time segment of the audio file (in seconds) to plot
time = np.linspace(2, length-2, num=data.shape[0])

if len(data.shape) == 1:
    # Mono audio
    plt.plot(time, data)
else:
      # Stereo audio
      plt.plot(time, data[:, 0], label="Left Channel")
      plt.plot(time, data[:, 1], label="Right Channel")

plt.legend( )
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Sound Wave Graph")
plt.grid(True)
plt.show()