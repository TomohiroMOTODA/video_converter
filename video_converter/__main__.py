import glob
import os
import subprocess

def compress_videos():
    videos = glob.glob('./data/*.mp4')
    for video in videos:
        os.rename(video, video.replace(' ', ''))
        
    videos = glob.glob('./data/*.mp4')
    count = 0
    for video in videos:
        os.makedirs('./data/compressed/', exist_ok=True)
        size = os.path.getsize(video)
        if size > 400000000:
            out = os.path.basename(video)
            out = out.split('_')[0]+"_task_video.mp4"
            out = os.path.join('./data/compressed', out)
            subprocess.call('ffmpeg -i '+video+' -crf 30 -vf "scale=-2:720" '+out, shell=True)
            count += 1

if __name__=="__main__":
    compress_videos()
