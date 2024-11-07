import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the WAV file (replace "sounds/radar.wav" with your actual file path)
sample_rate, data = wavfile.read("sounds/radar.wav")

length = data.shape[0] / sample_rate
print(f"length = {length}s")
# Select a smaller segment of data to visualize (e.g., first 0.7 seconds)
time = np.linspace(0., length, data.shape[0])
# Mono audio
plt.plot(time, data, label="Mono Channel")
# Stereo audio
# plt.plot(time, data[:, 0], label="Left Channel")
# plt.plot(time, data[:, 1], label="Right Channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()