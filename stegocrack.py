import argparse
import os
from modules import lsb_audio, spectrogram, metadata, hidden_file_scan

def main():
    parser = argparse.ArgumentParser(
        description="Audio Steganography CTF Tool - Stegocrack"
    )
    parser.add_argument(
        "-f", "--file",
        required=True,
        help="Path to the input WAV/MP3 audio file"
    )
    parser.add_argument(
        "--lsb",
        action="store_true",
        help="Extract hidden data using LSB technique"
    )
    parser.add_argument(
        "--spectrogram",
        action="store_true",
        help="Generate a spectrogram image from the audio"
    )
    parser.add_argument(
        "--metadata",
        action="store_true",
        help="Extract metadata from the audio file"
    )
    parser.add_argument(
        "--scan",
        action="store_true",
        help="Scan for hidden strings or embedded files"
    )
    parser.add_argument(
        "-o", "--output",
        default="output/",
        help="Output directory to save results"
    )

    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"[!] File not found: {args.file}")
        return

    if not args.file.lower().endswith((".wav", ".mp3")):
        print(f"[!] Only WAV or MP3 files are supported.")
        return

    os.makedirs(args.output, exist_ok=True)

    if args.lsb:
        print("[*] Running LSB extraction...")
        lsb_out = os.path.join(args.output, "lsb_output.txt")
        lsb_audio.extract_lsb_message(args.file, lsb_out)

    if args.spectrogram:
        print("[*] Generating spectrogram...")
        spectrogram_out = os.path.join(args.output, "spectrogram.png")
        spectrogram.generate_spectrogram(args.file, spectrogram_out)

    if args.metadata:
        print("[*] Extracting metadata...")
        metadata_out = os.path.join(args.output, "metadata_output.txt")
        metadata.extract_metadata(args.file, metadata_out)

    if args.scan:
        print("[*] Scanning for hidden files/strings...")
        scan_out = os.path.join(args.output, "hidden_file_strings.txt")
        hidden_file_scan.scan_hidden_files(args.file, scan_out)

    if not any([args.lsb, args.spectrogram, args.metadata, args.scan]):
        print("[!] Please specify at least one analysis mode:")
        print("    --lsb | --spectrogram | --metadata | --scan")

if __name__ == "__main__":
    main()
