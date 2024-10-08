from yt_dlp import YoutubeDL
import os
import shutil
from pathlib import Path
from pydantic import HttpUrl
from enum import Enum

from config.environment import FFMPEG_PATH


class OutputType(Enum):
    MP3 = "mp3"


class YouTubeHandler:
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)

        self._create_output_directory()

    def _create_output_directory(self):
        os.makedirs(self.output_dir)

    def _check_ffmpeg_installed(self):
        """Check if FFmpeg exists."""
        ffmpeg_path = Path(FFMPEG_PATH)
        if ffmpeg_path.is_file() or shutil.which(FFMPEG_PATH):
            return True
        else:
            print(f"FFmpeg not found at {FFMPEG_PATH}.")
            return False

    def download_video(self, youtube_url: HttpUrl, output_type: OutputType):
        if not self._check_ffmpeg_installed():
            raise RuntimeError(
                "FFmpeg is not installed. Please install FFmpeg and add it to PATH to proceed."
            )

        ydl_options = {
            "format": "bestaudio/best",
            "extractaudio": True,
            "audioformat": output_type,
            "outtmpl": str(self.output_dir / "%(title)s.%(ext)s"),
            "ffmpeg_location": str(FFMPEG_PATH),
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",  # 320 kbps, max bitrate for mp3
                }
            ],
            "noplaylist": True,
            "source_address": None,
            "quiet": True,
        }

        with YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(youtube_url, download=True)
            return str(self.output_dir / f"{info['title']}.mp3")
