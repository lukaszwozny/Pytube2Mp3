from cx_Freeze import setup, Executable

base = None

executables = [Executable("downloader.py", base=base)]

packages = ["idna", "os", "youtube_dl", "queue", "threading", "tkinter"]
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
