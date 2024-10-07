import re
from pydantic import HttpUrl


class InputHandler:
    def __init__(self):
        self.youtube_url_input = ""

    def _get_youtube_url_input(self):
        """Prompt the user for a YouTube URL."""
        self.youtube_url_input = input("Enter the YouTube URL for the original video: ")

    def _validate_youtube_url_input(self, youtube_url: HttpUrl):
        """Validate the YouTube URL format."""
        pattern = r"^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$"
        return re.match(pattern, youtube_url) is not None

    def get_valid_youtube_url(self):
        """Prompt the user for a valid YouTube URL."""
        while True:
            self._get_youtube_url_input()
            if self._validate_youtube_url_input(self.youtube_url_input):
                return self.youtube_url_input
            else:
                print("Invalid YouTube URL. Please try again.")
