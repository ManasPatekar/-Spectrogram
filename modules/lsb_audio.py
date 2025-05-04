import wave
import numpy as np
import os

def extract_lsb_message(wav_file, output_dir="output", output_txt="lsb_output.txt", output_bin="lsb_output.bin", delimiter="~"):
    try:
        # Open WAV file
        with wave.open(wav_file, mode='rb') as audio:
            n_frames = audio.getnframes()
            frames = audio.readframes(n_frames)
            frame_bytes = np.frombuffer(frames, dtype=np.uint8)

        # Extract LSBs
        extracted_bits = [str(byte & 1) for byte in frame_bytes]
        binary_str = ''.join(extracted_bits)

        # Group bits into bytes
        bytes_list = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]

        message_bytes = bytearray()
        for byte in bytes_list:
            if len(byte) < 8:
                break
            char = int(byte, 2)
            if chr(char) == delimiter:
                break
            message_bytes.append(char)

        # Ensure output dir exists
        os.makedirs(output_dir, exist_ok=True)

        # Save as binary
        bin_path = os.path.join(output_dir, output_bin)
        with open(bin_path, 'wb') as f:
            f.write(message_bytes)

        # Try decoding as text
        try:
            text = message_bytes.decode('utf-8')
            txt_path = os.path.join(output_dir, output_txt)
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"[+] LSB message extracted and saved to: {txt_path}")
        except UnicodeDecodeError:
            print("[-] Message contains binary data; saved to .bin file instead.")

        return message_bytes

    except Exception as e:
        print(f"[!] Error extracting LSB: {e}")
        return None

# CLI usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python lsb_audio.py <input.wav>")
    else:
        extract_lsb_message(sys.argv[1])
