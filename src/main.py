from classes.YouTubeHandler import YouTubeHandler
from classes.FileManager import FileManager
from classes.InputHandler import InputHandler


def main():
    file_manager = FileManager()

    try:
        input_handler = InputHandler()

        input_handler.get_valid_youtube_url()
        print(f"Valid YouTube URL: {input_handler.youtube_url_input}")

        with file_manager.create_temp_dir() as temp_dir:
            print(f"Temporary directory created: {temp_dir}")

            youtube_handler = YouTubeHandler(f"{temp_dir}/full_audio")
            mp3_path = youtube_handler.download_as_mp3(input_handler.youtube_url_input)

            print(f"MP3 file downloaded: {mp3_path}")

        # presentation_builder = PresentationBuilder('test', 'متكلم', 'speaker', 'نص', 'text')
    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    main()
