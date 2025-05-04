# 🔍 AudioStegoCrack

**AudioStegoCrack** is a powerful CLI tool designed for CTF players, security researchers, and forensic analysts to extract hidden data from audio files (WAV format). It automates multiple steganalysis techniques like LSB extraction, spectrogram generation, metadata analysis, and hidden file/string scanning.

---

## 🚀 Features

- 🔎 **LSB Extraction**: Extracts hidden messages embedded using Least Significant Bit technique.
- 🎵 **Spectrogram Analysis**: Visualizes frequency-based hidden data.
- 🧾 **Metadata Extraction**: Retrieves audio file metadata (EXIF, tags, etc.).
- 🕵️ **Hidden File & String Scan**: Identifies embedded files, suspicious strings, or markers.

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/ManasPatekar/Spectrogram-Detector.git
cd audiostegocrack

# Create and activate virtual environment (Windows)
python -m venv venv
.\venv\Scripts\Activate.ps1  # or .\venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt

#Run Command
python stegocrack.py -f "your_audio_file.wav" --lsb --spectrogram --metadata --scan -o output/

