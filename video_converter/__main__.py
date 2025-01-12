import glob
import os
import subprocess

from .libs.load_param import load_yaml

def compress_videos():
    config=load_yaml('./configs/param.yaml')
    quality  = config['compress']['quality']
    out_dir  = config['compress']['output']
    data_dir = config['compress']['input']
    
    videos = glob.glob(os.path.join(data_dir, '*.mp4'))
    for video in videos:
        os.rename(video, video.replace(' ', ''))

    videos = glob.glob('./data/*.mp4')
    count = 0
    for video in videos:
        os.makedirs('./data/compressed/', exist_ok=True)
        size = os.path.getsize(video)
        if size > 5000000:
            out = os.path.basename(video)
            out = out.split('_')[0]+"_task_video.mp4"
            out = os.path.join(out_dir, out)
            subprocess.call('ffmpeg -i '+video+' -crf '+str(quality)+' -vf "scale=-2:720" '+out, shell=True)
            count += 1

if __name__=="__main__":
    compress_videos()
