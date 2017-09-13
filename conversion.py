import ntpath
import shutil
import os
from urllib.error import URLError

from pytube import YouTube
import moviepy.editor as mp


class Converter:
    def get_yt_title(url):
        try:
            yt = YouTube(url=url)
            return yt.title
        except ValueError:
            return 'ERROR'

    def download_yt_video(url, on_progress=None):
        video_dir = 'tmp'
        if not os.path.exists(video_dir):
            os.makedirs(video_dir)
        try:
            yt = YouTube(url=url)
        except ValueError:
            raise ValueError
        except URLError:
            raise URLError
        extension = 'mp4'
        vid_path = video_dir + '/' + yt.filename + '.' + extension
        video = yt.filter(extension)[0]
        try:
            video.download(path=video_dir, force_overwrite=True, on_progress=on_progress)
        except URLError:
            raise URLError
        return vid_path

    def convert_video_to_mp3(vid_path):
        clip = mp.VideoFileClip(vid_path)
        vid_filename = ntpath.basename(vid_path)
        mp3_filename = ntpath.splitext(vid_filename)[0] + '.mp3'
        clip.audio.write_audiofile(filename=mp3_filename,
                                   progress_bar=False)
        del clip.reader
        del clip
        # Move mp3 to mp3/
        mp3_dir = 'mp3'
        if not os.path.exists(mp3_dir):
            os.makedirs(mp3_dir)
        shutil.move(mp3_filename, mp3_dir + '/' + mp3_filename)
        os.remove(str(vid_path))
