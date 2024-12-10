import numpy as np

# * Converting a waveform to decibels (dB)
#    - Decibels (dB) are a logarithmic unit used to express the ratio between two values, such as power or amplitude.
#  FORMULA: dB = 10 * log10(P / P0) - this formula calculates the logarithmic nature of decibels.
#    - dB is the sound intensity level in decibels.
#    - P is the power or amplitude of the signal.
#    - P0 is the reference power or amplitude (usually 1 micropascal for sound waves) which is 1e-6.


def wave_to_db(waveform):
      """
      Converts a waveform to decibels (dB).
   
      Args:
         waveform (np.array): represents the input waveform.
   
      Returns:
         np.array: The waveform in decibel values.
      """

      # Calculate the squared amplitude
      sq_amplitude = waveform ** 2

      # Calculate the mean squared amplitude
      mean_squared_amplitude = np.mean(sq_amplitude)

      # Convert to decibels (dB)
      decibles = 10 * np.log10(mean_squared_amplitude / 1e-6)

      return decibles


# Example usage of wave_to_db function
waveform = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
decibles = wave_to_db(waveform)
print(f"Decibles: {decibles}")


# Using RMS value
def wave_to_db_rms(waveform):
      """
      Converts a waveform to decibels (dB) using the RMS value.
   
      Args:
         waveform (np.array): represents the waveform.
   
      Returns:
         np.array: The waveform in decibel values.
      """

      # Calculate the squared amplitude
      sq_amplitude = np.mean(waveform ** 2)

      # Calculate the RMS value
      rms_value = np.sqrt(sq_amplitude)

      # Convert to decibels (dB)
      decibles = 20 * np.log10(rms_value / 1e-6)

      return decibles 

