import moviepy.editor as Koy
diomer = Koy.VideoFileClip('DarkRave.mp4')
diomer.audio.write_audiofile('Lightrave.mp3')
print(help)