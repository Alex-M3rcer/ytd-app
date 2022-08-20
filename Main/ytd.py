from colorsys import yiq_to_rgb
from turtle import down
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
    return download_completed()
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
    # when download is doen call Download dialoge
    # TODO: V0.9.0 Download complete Error handling
    return download_completed()
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
    

# when download compelted call show_complete_dialog from Form
def download_completed():
    return True
    # TODO: 0.9.0 Error handling for if download was completed or not
