from cx_Freeze import setup, Executable

base = None

executables = [Executable("downloader.py", base=base)]

packages = ["idna", "time", "winsound", "os", "youtube_dl", "queue", "threading", "tkinter", "pyperclip"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="downloader",
    options=options,
    version="1.0",
    description='Pobierak youtubowy',
    executables=executables
)
