import os
import soundfile as sf


class AudioHelper:
    @staticmethod
    def get_audio_duration(file_path):
        """
        Get the duration of an audio file.

        Args:
            file_path (str): The path to the audio file.

        Returns:
            float: The duration in seconds, or None if the duration cannot be determined.
        """
        try:
            info = sf.info(file_path)
            return info.duration if info else None
        except Exception as e:
            print(f"Error getting audio duration: {str(e)}")
            return None

    @staticmethod
    def get_audio_type(file_path):
        """
        Get the audio type (file extension) of an audio file.

        Args:
            file_path (str): The path to the audio file.

        Returns:
            str: The audio type (e.g., '.wav', '.mp3', etc.).
        """
        try:
            _, file_extension = os.path.splitext(file_path)
            return file_extension
        except Exception as e:
            print(f"Error getting audio type: {str(e)}")
            return None

    @staticmethod
    def get_audio_content(file_path):
        """
        Get the content of an audio file as bytes.

        Args:
            file_path (str): The path to the audio file.

        Returns:
            bytes: The content of the audio file as bytes.
        """
        try:
            with open(file_path, "rb") as file:
                return file.read()
        except Exception as e:
            print(f"Error getting audio content: {str(e)}")
            return None
