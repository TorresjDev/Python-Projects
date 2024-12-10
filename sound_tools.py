import numpy as np
# ! Converting a waveform to decibels (dB)
#    - Decibels (dB) are a logarithmic unit used to express the ratio between two values, such as power or amplitude.
#  FORMULA: dB = 10 * log10(P / P0) - this formula calculates the logarithmic nature of decibels.
#    - dB is the sound intensity level in decibels.
#    - P is the power or amplitude of the signal.
#    - P0 is the reference power or amplitude (usually 1 micropascal for sound waves) which is 1e-6.


# * Converting a waveform to decibels (dB)
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


# * Converting a waveform to decibels (dB) using the RMS value
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


# Find the highest and smallest dB levels
def detect_db_range(waveform):
    """
    Detects the highest and smallest dB levels in a waveform.

    Args:
        waveform: A numpy array representing the waveform.

    Returns:
        tuple: (highest_dB, smallest_dB)
    """
    db_values = wave_to_dbfs(waveform)  # Convert waveform to dBFS
    highest_dB = np.max(db_values)  # Maximum dB level
    smallest_dB = np.min(db_values)  # Minimum dB level
    return highest_dB, smallest_dB


# * Converting a waveform to decibels relative to full scale (dBFS)
def wave_to_dbfs(waveform):
    """
    Converts a waveform to decibels relative to full scale (dBFS).

    Args:
        waveform: A numpy array representing the waveform.

    Returns:
        A numpy array of dBFS values.
    """
    max_value = np.iinfo(waveform.dtype).max  # Maximum possible value for the waveform's data type
    epsilon = 1e-10  # Small value to avoid log10(0)
    
    # Ensure no zeros are passed to log10 by replacing zeros with a small value
    decibels = 20 * np.log10(np.maximum(np.abs(waveform), epsilon) / max_value)
    return decibels


