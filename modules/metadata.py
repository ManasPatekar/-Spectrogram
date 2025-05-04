from mutagen.wave import WAVE
from mutagen.id3 import ID3
from mutagen.mp3 import MP3
import os

def extract_metadata(file_path, output_txt="metadata_output.txt"):
    try:
        info = ""
        if file_path.lower().endswith(".wav"):
            audio = WAVE(file_path)
            info += str(audio.tags or "No metadata found.")
        elif file_path.lower().endswith(".mp3"):
            audio = MP3(file_path, ID3=ID3)
            for tag in audio.tags.values():
                info += f"{tag}\n"
        else:
            info = "Unsupported format for metadata extraction."

        os.makedirs(os.path.dirname(output_txt), exist_ok=True)
        with open(output_txt, "w") as f:
            f.write(info)

        print(f"[+] Metadata extracted to {output_txt}")
        return info

    except Exception as e:
        print(f"[!] Error extracting metadata: {e}")
        return None
