import os
from openai import OpenAI
from app.config.config import Config
import yt_dlp



def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'verbose': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return ydl.prepare_filename(ydl.extract_info(url, download=False))


def transcribe_audio(audio_path):
    client = OpenAI(api_key=Config.OPENAI_API_KEY)
    # replace file extension with .mp3
    base, _ = os.path.splitext(audio_path)
    audio_path = os.path.join(os.getcwd(), f"{base}.mp3")
    audio_file= open(audio_path, "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    return transcription.text


def get_transcription(url):
    audio_path = download_audio(url)
    transcription = transcribe_audio(audio_path)
    return transcription