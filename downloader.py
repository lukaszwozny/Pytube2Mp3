import youtube_dl
import os
import queue
import threading

from tkinter import *
import tkinter.ttk as ttk

# Download data and config

download_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Song Directory
if not os.path.exists('Songs'):
    os.mkdir('Songs')
else:
    os.chdir('Songs')


def download(song_url):
    with youtube_dl.YoutubeDL(download_options) as dl:
        info_dict = dl.extract_info(song_url, download=True)

        video_title = info_dict.get('title', None)
        print(video_title)
        # dl.download([song_url])
        return video_title


class ThreadedTask(threading.Thread):
    def __init__(self, queue, url):
        threading.Thread.__init__(self)
        self.queue = queue
        self.url = url

    def run(self):
        try:
            title = download(self.url)
            self.queue.put(title)
        except:
            self.queue.put("ERROR")


class EntryFrame(Frame):

    def __init__(self, master, parent):
        super(EntryFrame, self).__init__(master)

        self.parent = parent

        self.entry = Entry(self, width=100, justify="right")
        self.entry.pack(side=LEFT, fill=Y, padx=10)

        self.test_button = Button(self, command=self.on_click)
        self.test_button.configure(
            text="Pobierz", background="Lightgreen", fg="darkgreen",
            padx=50
        )
        self.test_button.pack()

    def on_click(self):
        text = self.entry.get()
        if text == '':
            return

        self.entry.delete(0, END)

        self.parent.populate(text)


class WidgetItem(Frame):

    def __init__(self, master, url):
        super(WidgetItem, self).__init__(master)
        self.url = url

        self.label = Label(self, text=self.url, width=95)
        self.label.pack(side=LEFT)

        self.prog_bar = ttk.Progressbar(
            self, orient="horizontal",
            length=100, mode="indeterminate"
        )
        self.prog_bar.pack(side=TOP)
        self.prog_bar.start()

        self.queue = queue.Queue()
        ThreadedTask(self.queue, self.url).start()
        self.master.after(100, self.process_queue)

    def process_queue(self):
        try:
            msg = self.queue.get(0)
            self.prog_bar.stop()
            self.prog_bar.pack_forget()
            print(msg)
            if msg == 'ERROR':
                Label(self, text="BŁĄD", fg='Red').pack(side=TOP)
            else:
                Label(self, text="UKOŃCZONO", fg='Green').pack(side=TOP)
                self.label['text'] = msg
        except queue.Empty:
            self.master.after(100, self.process_queue)


class GUI:
    def __init__(self, master):
        self.master = master

        self.entry_frame = EntryFrame(master, self)
        self.entry_frame.pack(padx=10, pady=10)

        canvas = Canvas(master, borderwidth=0, background="#ffffff")
        self.frame = Frame(canvas, background="#ffffff")
        vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4, 4), window=self.frame, anchor="nw")

        self.frame.bind("<Configure>", lambda event, canvas=canvas: self.onFrameConfigure(canvas))

    def onFrameConfigure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    def populate(self, title):
        '''Put in some fake data'''

        WidgetItem(self.frame, title).pack(anchor='n')
        # Label(frame, text="%s" % row, width=3, borderwidth="1",
        #          relief="solid").grid(row=row, column=0)
        # t = "this is the second column for row %s" % row
        # Label(frame, text=t).grid(row=row, column=1)


def progress(self):
    self.prog_bar = ttk.Progressbar(
        self.master, orient="horizontal",
        length=200, mode="indeterminate"
    )
    self.prog_bar.pack(side=BOTTOM)


def tb_click(self):
    self.progress()

    self.test_button['state'] = 'disabled'

    self.prog_bar.start()
    self.queue = queue.Queue()
    ThreadedTask(self.queue).start()
    self.master.after(100, self.process_queue)
    # Simulate long running process
    # t = threading.Thread(target=time.sleep, args=(5,))
    # t.start()
    # t.join()
    # self.prog_bar.stop()


def process_queue(self):
    try:
        msg = self.queue.get(0)
        print(msg)
        self.test_button['state'] = 'normal'
        # Show result of the task if needed
        self.prog_bar.stop()
    except queue.Empty:
        self.master.after(100, self.process_queue)


root = Tk()
root.title("Test Button")
main_ui = GUI(root)
root.mainloop()
