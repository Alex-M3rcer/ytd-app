from colorsys import yiq_to_rgb
from dataclasses import field
from turtle import down
from pytube import YouTube, exceptions
import os


# NOTE: custom Exceptions
class QualityNotFound(Exception):
    def __init__(self, msg='Quality For this video was not found'):
        super().__init__(msg)


# return youtube video's Title and Thumbnail video
def get_infos(link):
    yt = YouTube(link)
    
    return yt.thumbnail_url, yt.title

# Download the video MP4
def video_download(url, quality, download_path):

    yt = YouTube(url)
    # [ ] Learn about the callback system
    # [ ] V1.4.0 make Callback function for progress bar
    #yt.register_on_complete_callback(callable=download_callable)

    # NOTE: try stream if None Except for quality not found
    try:
        stream = get_video_stream(yt,quality)
        out_file = stream.download(download_path)

        base = os.path.splitext(out_file)[0]
        ext = 1
        try:
            new_file = base + '.mp4'
            os.rename(out_file, new_file)
        except FileExistsError:
            #* this will try to rename the file even if it exists it will create new one with number at the end
            while True:
                new_file = base + str(ext) +'.mp4'
                try:
                    os.rename(out_file, new_file)
                    break
                except FileExistsError:
                    ext += 1
                    continue
        return download_completed(new_file)
    except  QualityNotFound:
        raise QualityNotFound
    

    
    # TODO: V0.9.0 add some error handling for download not wroking or quality not doesn't exist

# download Audio Only MP3
def audio_download(url , download_path):
    yt = YouTube(url)
    title = yt.title
    # NOTE: try stream if None Except for quality not found
    try:
        stream = get_audio_stream(yt)

        # Save the file and change its ext to mp3
        out_file = stream.download(download_path)
        base = os.path.splitext(out_file)[0]
        
        ext = 1
        try:
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        except FileExistsError:
            #* this will try to rename the file even if it exists it will create new one with number at the end
            while True:
                new_file = base + str(ext) +'.mp3'
                try:
                    os.rename(out_file, new_file)
                    break
                except FileExistsError:
                    ext += 1
                    continue
                
            
        # when download is doen call Download dialoge
        return download_completed(new_file)
    except QualityNotFound:
        raise QualityNotFound


# Get Streams for Audio and Video
def get_video_stream(yt,quality):
    if quality:
        if quality == 'Highest Resolution':
            stream = yt.streams.filter(progressive=True).get_highest_resolution()
        else:
            stream = yt.streams.filter(progressive=True).get_by_resolution(quality)
    if stream == None:
        raise QualityNotFound
    else:
        return stream

def get_audio_stream(yt):
    stream = yt.streams.get_audio_only('mp4')
    if stream == None:
        raise QualityNotFound
    else:
        return stream
    

# when download compelted call show_complete_dialog from Form
def download_completed(file_path):
    print(file_path)
    if os.path.exists(file_path):
        return True
    else:
        return False


# [ ] V1.4.0 make Callback function for progress bar
def download_callable(stream,file_path):
    print('called')
    print(file_path)
    if os.path.exists(file_path):
        print('Downloaded')
    else:
        print('shit')
    print('Done')