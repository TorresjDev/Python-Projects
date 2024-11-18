# Sound Wave Analysis Project

This project visualizes sound wave data from a `.wav` file, plotting it as a graph to analyze its amplitude over time. The program is implemented in Python using libraries such as NumPy, Matplotlib, and SciPy.

---

## Step-by-Step Code Explanation

1. **Import Required Libraries**:

   - `numpy`: For numerical operations.
   - `matplotlib.pyplot`: To create the graph.
   - `scipy.io.wavfile`: To read `.wav` audio files.

2. **Load the WAV File**:

   - Replace the path `"sounds/decibel-stps-x10.wav"` with your own `.wav` file path.

3. **Extract Data**:

   - The sample rate and audio data are extracted using `wavfile.read()`.

4. **Calculate Audio Length**:

   - Compute the duration of the audio using `length = data.shape[0] / sample_rate`.

5. **Prepare Time Axis**:

   - Create a time axis array (`time`) based on the sample rate and data length.

6. **Plot the Audio Wave**:
   - Plot the amplitude (vertical axis) against time (horizontal axis).
   - Add labels and a legend for clarity.
   - Use `plt.show()` to display the graph.

---

## How to Run the Code Locally

1. **Install Required Libraries**:

   - Ensure you have Python installed on your machine.
   - Install the required libraries by running:
     ```bash
     pip install numpy matplotlib scipy
     ```

2. **Run in Jupyter Notebook**:

   - Install Jupyter Notebook if you don't have it:
     ```bash
     pip install notebook
     ```
   - Launch Jupyter Notebook by typing in your terminal:
     ```bash
     jupyter notebook
     ```
   - Open the `.ipynb` file in the Jupyter interface.

3. **Run the Script**:

   - Open the `sound_wave_analysis.ipynb` or `.py` file in Jupyter.
   - Execute the code cells by clicking the "Run" button or pressing `Shift + Enter`.

4. **View the Graph**:
   - After running the last cell, the graph will appear, visualizing the audio waveform.

---

## Alternative: Running in Visual Studio Code

1. **Install Python Extension**:

   - Ensure the Python extension is installed in Visual Studio Code.

2. **Open the Project**:

   - Open the folder containing the `.py` file.

3. **Run the File**:

   - Open the terminal in Visual Studio Code (`Ctrl + ``).
   - Type the following to run the script:
     ```bash
     python sound_wave_analysis.py
     ```

4. **View the Graph**:
   - The graph will appear in a new window.

---

### Notes:

- Make sure to replace `"sounds/decibel-stps-x10.wav"` in the code with your actual `.wav` file path.
- If working with stereo audio, uncomment the relevant lines in the script to handle left and right audio channels separately.
