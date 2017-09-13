from enum import Enum

from kivy.properties import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from multiprocessing.dummy import Pool as ThreadPool

from conversion import Converter
import threading
import time

scroll_items = []
MAX_SIZE = 4


class Status(Enum):
    WAITING = 'Waiting'
    DOWNLOADING = 'Downloading'
    CONVERTING = 'Converting'
    DONE = 'Done'


class ScrollItem(BoxLayout):
    # height = 50
    # label = Label()
    stop = threading.Event()

    def __init__(self, text, **kwargs):
        super(ScrollItem, self).__init__(**kwargs)
        self.padding = 2
        self.height = 30
        self.size_hint_y = None
        # Add labels
        self.title_label = Label()
        self.title_label.text = text
        self.title_label.size_hint = (0.7, 1)
        self.status_label = Label()
        self.status_label.text = Status.WAITING.value
        self.status_label.size_hint = (0.2, 1)
        self.add_widget(self.title_label)
        self.add_widget(self.status_label)
        # Add progress bars
        self.download_bar = ProgressBar()
        self.download_bar.value = 0
        self.download_bar.size_hint = (0.1, 1)
        self.add_widget(self.download_bar)

        Clock.schedule_interval(self.update, 1 / 20.)
        print(len(scroll_items))
        self.url = 'https://www.youtube.com/watch?v=vGRC2LYmHfU'
        # self.result = pool.map(Converter.download_yt_video, [url, ])

    def update(self, *args):
        if self.download_bar.value == 100:
            pass
        if self in scroll_items:
            # self.progressbar.value += 1
            if self.download_bar.value >= 100:
                scroll_items.remove(self)
        else:
            if self.download_bar.value < 100 and len(scroll_items) < MAX_SIZE:
                scroll_items.append(self)
                self.start_download()

    def start_download(self):
        threading.Thread(target=self.download_thread, args=(self.url,)).start()

    def download_thread(self, url):
        self.status_label.text = Status.DOWNLOADING.value
        vid_path = Converter.download_yt_video(url=url, on_progress=self.update_progressbar)
        self.start_converter(vid_path)

    def update_progressbar(self, bytes_recieved, file_size, start_datatime):
        self.download_bar.value = bytes_recieved / file_size * 100

    def start_converter(self, vid_path):
        self.status_label.text = Status.CONVERTING.value
        Converter.convert_video_to_mp3(vid_path)
        self.status_label.text = Status.DONE.value
