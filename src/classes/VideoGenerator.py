import win32com.client
import time
import os
from pathlib import Path


class VideoGenerator:
    def __init__(self, pptx_path: Path, output_path: Path):
        self.pptx_path = pptx_path
        self.output_path = output_path

    def generate_mp4_from_pptx(self):
        # Start PowerPoint
        try:
            PowerPoint = win32com.client.Dispatch("PowerPoint.Application")
        except Exception as e:
            print(f"Error initializing PowerPoint: {e}")
            return

        # Open the PPTX
        try:
            presentation = PowerPoint.Presentations.Open(
                self.pptx_path, WithWindow=False
            )
        except Exception as e:
            print(f"Error opening presentation: {e}")
            PowerPoint.Quit()
            return

        # Create MP4
        try:
            presentation.CreateVideo(self.output_path, -1, 4, 720, 24, 60)
            print("Video creation started...")

            start_time = time.time()
            while True:
                time.sleep(4)
                if (
                    os.path.isfile(self.output_path)
                    and os.path.getsize(self.output_path) > 0
                ):
                    print("Video creation successful!")
                    break
                if time.time() - start_time > 60 * 10:
                    print("Video creation timed out.")
                    break

        except Exception as e:
            print(f"Error creating video: {e}")

        finally:
            presentation.Close()
            PowerPoint.Quit()
