import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import os

def generate_spectrogram(wav_path, output_img="spectrogram.png"):
    try:
        rate, data = wav.read(wav_path)

        if data.ndim > 1:
            data = data[:, 0]  # Use only the first channel if stereo

        plt.figure(figsize=(12, 6))
        plt.specgram(data, Fs=rate, NFFT=1024, noverlap=512, cmap='inferno')
        plt.title("Spectrogram")
        plt.xlabel("Time")
        plt.ylabel("Frequency")

        os.makedirs(os.path.dirname(output_img), exist_ok=True)
        plt.savefig(output_img, dpi=300)
        plt.close()
        print(f"[+] Spectrogram saved to: {output_img}")
        return output_img

    except Exception as e:
        print(f"[!] Error generating spectrogram: {e}")
        return None

# For direct testing
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python spectrogram.py <input.wav>")
    else:
        generate_spectrogram(sys.argv[1])
