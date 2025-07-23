# 🎶 **Sound Wave Analysis Project** 🌊

<p align="center">
  <img src="https://torresjdev.github.io/Nextjs-Asset-Host/assets/covers/projects/sound-wave-analysis-project.png" alt="Sound Wave Analysis" width="300"/>
</p>

A **Visual representation tool** for **Physics - Sound Waves** analysis using Python. This application leverages the latest features and libraries to provide an intuitive interface for analyzing sound waves and generating detailed visualizations. This program is a terminal-based application that allows users to interactively select audio files, perform various analyses, and visualize the results in a clean and professional manner.

---

## ✨ **Key Features**

### 🎮 **Enhanced User Experience**

- **Arrow Key Navigation** - Navigate through files and options with ↑ & ↓ keys
- **Interactive File Selection** - Visual selection with real-time highlighting
- **Clean Interface** - Professional terminal interface with clear visual feedback
- **Intuitive Controls** - Enter to select, 'q' to quit, Esc for quick exit

### 🎧 **Advanced Audio Analysis**

- **Waveform Visualization** - Time-domain amplitude analysis
- **Frequency Spectrogram** - Detailed frequency analysis over time
- **Comprehensive dB Analysis** - Peak, RMS, dynamic range calculations
- **Multi-format Support** - Handles mono and stereo WAV files
- **Export Options** - Save visualizations as high-quality PNG files

### 🏗️ **Professional Architecture**

- **Modular Design** - Clean separation of concerns
- **Scalable Structure** - Easy to extend and maintain
- **Import Optimization** - Each module imports only what it needs
- **Error Handling** - Robust error management and user feedback

---

## 🚀 **Quick Start**

### 1️⃣ **Installation**

```bash
# Clone the repository
git clone https://github.com/TorresjDev/Python-Sound-Wave-Analysis.git
cd Python-Sound-Wave-Analysis

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ **Add Your Audio Files**

Place your `.wav` files in the `data/` directory:

```bash
# Your structure should look like this:
data/
├── your_audio_file1.wav
├── your_audio_file2.wav
└── sample_audio.wav
```

### 3️⃣ **Run the Application**

```bash
python main.py
```

**🎮 Interactive Experience:**

1. Use ↑/↓ arrow keys to navigate through WAV files
2. Press Enter to select your desired file
3. Choose analysis options with the same intuitive navigation
4. Enjoy beautiful visualizations and detailed analysis!

---

## 📁 **Professional Project Structure**

```
Python-Sound-Wave-Analysis/
│
├── main.py                     # 🚀 Clean entry point (main function only)
├── requirements.txt            # 📦 Project dependencies
├── LICENSE                     # ⚖️ MIT License
├── README.md                   # 📖 Complete documentation
├── .gitignore                  # 🙈 Git ignore rules
│
├── sound_analysis/             # 🏗️ Core analysis package
│   ├── analyzer.py             # 🔬 WAV processing & analysis engine
│   ├── tools.py               # 🛠️ Math functions & user interface
│   └── visualization.py       # 🎨 Matplotlib plotting functions
│
├── data/                       # 📊 Your audio files go here
│   ├── sample1.wav            # 🎵 Sample audio files
│   ├── sample2.wav
│   └── your_files.wav
│
├── figures/                    # 📈 Generated visualizations
│   └── [auto-generated plots]
│
└── notebooks/                  # 📓 Jupyter analysis notebooks
    └── sound-wave-analysis.ipynb
```

---

## 🎯 **Module Responsibilities**

### 🚀 **main.py**

- Single entry point with clean `main()` function
- Orchestrates the entire application flow
- Imports from modular components

### 🛠️ **sound_analysis/tools.py**

- Mathematical audio processing functions
- Enhanced user interface with arrow-key navigation
- File management utilities
- Fallback support for different environments

### 🔬 **sound_analysis/analyzer.py**

- Core WAV file processing
- Comprehensive audio analysis algorithms
- Error handling and data validation
- Integration with visualization components

### 🎨 **sound_analysis/visualization.py**

- All matplotlib-based plotting functions
- High-quality visualization generation
- Export capabilities for figures
- Multiple plot types (waveform, spectrogram, combined)

---

## 🎛️ **Analysis Options**

### **1. Standard Analysis**

- Waveform visualization
- Frequency spectrogram
- Real-time display

### **2. Save Figures**

- High-resolution PNG exports
- Organized in `figures/` directory
- Publication-ready quality

### **3. Analysis Only**

- Detailed numeric analysis
- No plot generation
- Fast processing mode

---

## 📊 **Technical Specifications**

### **Supported Formats**

- ✅ WAV files (16-bit, mono/stereo)
- ✅ Various sample rates
- ✅ Multiple bit depths

### **Analysis Metrics**

- 🔊 **Average dB** - Overall sound level
- 📊 **RMS dB** - Root Mean Square analysis
- 📏 **Dynamic Range** - Peak-to-minimum difference
- 📈 **Peak dB** - Maximum amplitude
- 📉 **Minimum dB** - Quietest detected level

### **Dependencies**

```python
numpy>=1.21.0       # Numerical computations
matplotlib>=3.5.0   # Visualization engine
scipy>=1.7.0        # Signal processing
keyboard>=0.13.5    # Enhanced user interface
wave>=0.0.2         # Audio file handling
```

---

## 🎓 **Key Audio Concepts**

- **🌊 Waveform** - Visual representation of amplitude over time
- **📏 Amplitude** - Wave height representing loudness/volume
- **🎵 Frequency** - Wave cycles per second (Hz), determines pitch
- **🔊 Decibels (dB)** - Logarithmic measure of sound intensity
- **📊 Spectrogram** - Time-frequency analysis showing pitch changes
- **🎛️ Dynamic Range** - Difference between loudest and quietest parts

---

## 🔧 **Development Features**

### **Code Quality**

- Clean, readable Python code
- Comprehensive documentation
- Type hints and docstrings
- Modular architecture

### **User Experience**

- Intuitive navigation
- Clear error messages
- Graceful error handling
- Cross-platform compatibility

### **Performance**

- Optimized audio processing
- Efficient memory usage
- Fast visualization rendering
- Scalable for large files

---

## 📈 **Example Output**

```
🌊 Welcome to Sound Wave Analysis!
========================================

🎵 Available WAV files:
==================================================
Use ↑/↓ arrows to navigate, Enter to select, 'q' to quit
==================================================
► your_audio.wav ◄
  another_file.wav
  sample_music.wav

✅ Selected: your_audio.wav

🎵 Analysis Results
========================================
📁 File: your_audio.wav
📊 Sample Rate: 44,100 Hz
⏱️  Duration: 3.45 seconds
🎧 Channels: 2 (Stereo)
📈 Total Samples: 152,460

📈 Sound Levels:
🔊 Average dB: 85.32
📊 RMS dB: 142.18
📏 Dynamic Range: 68.45 dB
📈 Max dB: 195.67
📉 Min dB: 127.22

🎨 Generating visualizations...
✅ Analysis completed!
```

---

## 🤝 **Contributing**

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Follow the modular architecture
4. Add comprehensive documentation
5. Submit a pull request

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **Python Audio Community** for excellent libraries
- **NumPy & SciPy** for powerful numerical computing
- **Matplotlib** for beautiful visualizations
- **Keyboard Library** for enhanced user interaction

---

**🎵 Happy Audio Analysis! 🌊**

_Built with ❤️ by TorresjDev_
