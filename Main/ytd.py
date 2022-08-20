from colorsys import yiq_to_rgb
from pytube import YouTube




def get_stream(link):
    yt = YouTube(link)



# return youtube video's Title and Thumbnail video
def get_infos(link):
    yt = YouTube(link)
    
    return yt.thumbnail_url, yt.title

def video_download(url,quality,download_path):

    yt = YouTube(url)
    stream = get_stream(yt,quality)
    stream.download(download_path)
    # TODO: V0.9.0 add some error handling for download not wroking or quality not doesn't exist

def get_stream(yt,quality):
    if quality:
        if quality == 'Highest Resolution':
            return yt.streams.filter(progressive=True).get_highest_resolution()
        else:
            return yt.streams.filter(progressive=True).get_by_resolution(quality)


