from colorsys import yiq_to_rgb
from pathlib import Path
import os
from pytube import YouTube

download_path = str(os.path.join(Path.home(), 'Downloads'))
print(download_path)


def get_stream(link):
    yt = YouTube(link)



# return youtube video's Title and Thumbnail video
def get_infos(link,proxy=False):
    yt = YouTube(link)
    
    return yt.title,yt.thumbnail_url