import sys
from time import sleep


class TextLoader:
    def __init__(self, title, speed = 0.05, trailingCrlf = True, crlifyAround = False, isInput = False):
        self.title = title
        self.speed = speed
        self.trailingCrlf = trailingCrlf
        self.crlifyAround = crlifyAround
        self.isInput = isInput
        self.process()

    def process(self):
        if self.crlifyAround: print()

        self.start()

        for i in range(len(self.title)):
            sleep(self.speed)
            self.progress(i)

        self.end()
        
        if (self.crlifyAround or self.trailingCrlf) and not self.isInput: print()

    def start(self):
        self.progress_x = 0
        sys.stdout.write("" + ""*len(self.title) + "")
        sys.stdout.flush()

    def progress(self, index):
        sys.stdout.write(self.title[index])
        sys.stdout.flush()

    def end(self):
        sys.stdout.write('\n' if not self.isInput else '')
        sys.stdout.flush()
    
