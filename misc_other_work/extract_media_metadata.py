# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:21:55 2025

@author: ifrommer
"""
import ffmpeg
import sys
from pprint import pprint # for printing Python dictionaries in a human-readable way

# read the audio/video file from the command line arguments
#media_file = "2023_07_26_11_32_58.mp4" #sys.argv[1]
media_file = "test_download.mp4"
# uses ffprobe command to extract all possible metadata from the media file
pprint(ffmpeg.probe(media_file)["streams"])

#%%
import subprocess
import json

def get_creation_date(file_path):
    """Extracts the creation date from an MP4 file using ffprobe."""
    try:
        command = [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-i", file_path
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        metadata = json.loads(result.stdout)
        
        if 'format' in metadata and 'tags' in metadata['format'] and 'creation_time' in metadata['format']['tags']:
             return metadata['format']['tags']['creation_time']
        else:
            return "Creation date not found in metadata"

    except subprocess.CalledProcessError as e:
        return f"FFprobe error: {e}"
    except json.JSONDecodeError:
         return "Error decoding FFprobe output"
    except FileNotFoundError:
        return "FFprobe not found. Ensure FFmpeg is installed and in your PATH."


# Example usage:
file_path = media_file #"your_video.mp4"  # Replace with the actual path to your MP4 file
creation_date = get_creation_date(file_path)
print(f"Creation date: {creation_date}")