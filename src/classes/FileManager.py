import os
import shutil
import tempfile
from pathlib import Path


class FileManager:
    def __init__(self, output_dir: Path = "output/"):
        self.output_dir = output_dir

        self._clean_output_directory()
        self._create_output_directory()

    def _create_output_directory(self):
        os.makedirs(self.output_dir)

    def _clean_output_directory(self):
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

    def create_temp_dir(self):
        return tempfile.TemporaryDirectory(dir=self.output_dir)
