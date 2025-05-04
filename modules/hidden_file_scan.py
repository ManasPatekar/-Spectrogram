import subprocess
import os

def scan_hidden_files(file_path, output_txt="hidden_file_strings.txt"):
    try:
        os.makedirs(os.path.dirname(output_txt), exist_ok=True)
        with open(output_txt, 'w') as f:
            subprocess.run(['strings', '-n', '4', file_path], stdout=f)

        print(f"[+] Strings scan saved to {output_txt}")
        return output_txt

    except Exception as e:
        print(f"[!] Error running strings scan: {e}")
        return None
