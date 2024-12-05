import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the WAV file (replace with your actual file path)
sample_rate, data = wavfile.read("sounds/decibel-stps-x10.wav")

# Step 2: Check if the audio is mono or stereo
if len(data.shape) == 2:
    # Stereo audio
    data = np.mean(data, axis=1)
    print("Stereo audio detected. Averaging channels.")
else:
    # Mono audio
    print("Mono audio detected.")

# Step 3: Calculate the RMS (Root Mean Square) amplitude
rms_amplitude = np.sqrt(np.mean(data**2))

# Step 4: Convert the amplitude to dB
amplitude_db = 20 * np.log10(rms_amplitude)
print(f"Amplitude in dB: {amplitude_db:.2f} dB")

# Step 5: Plot the results
time = np.arange(len(data)) / sample_rate
plt.figure(figsize=(10, 4))
plt.plot(time, data)
plt.title('Sound Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
# plt.tight_layout()
plt.show()
