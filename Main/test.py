from pytube import YouTube
import os


yt = YouTube('https://www.youtube.com/watch?v=23hjbOziaLM')
stream = yt.streams.get_audio_only('mp4')

out_file = stream.download('C:/Users/abmoh/Downloads/Compressed/1')
base = os.path.splitext(out_file)[0]
print(base)
new_file = base + '.mp3'
print(new_file)
os.rename(out_file, new_file)
print(stream)