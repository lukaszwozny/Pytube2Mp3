from pytube import YouTube


def download_yt_video(url, path):
    yt = YouTube(url=url)
    video = yt.filter('mp4')[0]
    video.download(path)


def main():
    url = 'https://www.youtube.com/watch?v=HgzGwKwLmgM'
    path = 'tmp'
    download_yt_video(url=url, path=path)


if __name__ == "__main__":
    main()
