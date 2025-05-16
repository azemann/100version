import subprocess, tempfile
from .loader_audio import transcribe_audio

def transcribe_video_audio(path):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    subprocess.run(["ffmpeg", "-i", path, "-vn", "-acodec", "libmp3lame", tmp.name])
    return transcribe_audio(tmp.name)
