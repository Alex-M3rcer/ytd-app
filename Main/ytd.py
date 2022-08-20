from colorsys import yiq_to_rgb
from pytube import YouTube
import os


# return youtube video's Title and Thumbnail video
def get_infos(link):
    yt = YouTube(link)
    
    return yt.thumbnail_url, yt.title

# Download the video MP4
def video_download(url, quality, download_path):

    yt = YouTube(url)
    stream = get_video_stream(yt,quality)
    stream.download(download_path)
    # TODO: V0.9.0 add some error handling for download not wroking or quality not doesn't exist

# download Audio Only MP3
def audio_download(url , download_path):
    yt = YouTube(url)
    stream = get_audio_stream(yt)

    # Save the file and change its ext to mp3
    out_file = stream.download(download_path)
    base = os.path.splitext(out_file)[0]
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    # TODO: V0.8.0 Download Complete Dialoge
    # TODO: V0.9.0 Error handling for audio not existing


# Get Streams for Audio and Video
def get_video_stream(yt,quality):
    if quality:
        if quality == 'Highest Resolution':
            return yt.streams.filter(progressive=True).get_highest_resolution()
        else:
            return yt.streams.filter(progressive=True).get_by_resolution(quality)

def get_audio_stream(yt):
    return yt.streams.get_audio_only('mp4')
    