import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io import wavfile

# sample_rate, data = wavfile.read("")
# print("Sample rate: ", sample_rate)
# print("Data shape:", data.shape)

# calculate time values for plotting
# time = np.linspace(0, len(data)/sample_rate, num=len(data))

# 
# log_data = 10 * np.log10(np.abs(data) + 1)

# plt.figure(figsize=(12, 6))
# plt.plot( log_data)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude [dB]")
plt.title("Sound wave analysis")
plt.show()