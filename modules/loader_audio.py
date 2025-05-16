import subprocess

def transcribe_audio(path):
    result = subprocess.run(["whisper", path, "--model", "base", "--language", "fr"],
                            capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else "Erreur de transcription"
