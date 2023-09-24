import sys
from time import sleep


class StartLoader:
    def __init__(self, title):
        self.title = title
        self.process()

    def process(self):
        self.start()

        for i in range(100):
            sleep(0.01)
            self.progress(i)
 
        self.end()

    def start(self):
        self.progress_x = 0
        sys.stdout.write(self.title + ": [" + "-"*18 + "]" + chr(8)*19)
        sys.stdout.flush()

    def progress(self, x):
        x = int(x * 18 // 100)
        sys.stdout.write("#" * (x - self.progress_x))
        sys.stdout.flush()
        self.progress_x = x

    def end(self):
        sys.stdout.write("#" * (18 - self.progress_x) + "]\n\n")
        sys.stdout.flush()
