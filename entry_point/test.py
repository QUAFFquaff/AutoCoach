

from PyQt5.QtCore import QThread, pyqtSignal
import threading
from queue import Queue
import time

class FeedbackController(QThread, threading.Thread):
    def __init__(self, q, cond:threading.Condition):
        super().__init__()
        self.q = q
        self.cond = cond
        print("init feedback")

    def run(self):
        print("feedback")
        with self.cond:
            while True:
                self.cond.wait()
                print(q.get())



class LDA(QThread,threading.Thread):
    def __init__(self, q, cond:threading.Condition):
        super().__init__()
        self.q = q
        self.cond = cond
        print("init lda")

    def run(self):
        print("lda")
        with self.cond:
            while True:
                time.sleep(10)
                q.put(3)
                self.cond.notify()



if __name__ == '__main__':
    q = Queue()
    cond = threading.Condition()
    f = FeedbackController(q, cond)
    f.start()
    l = LDA(q,cond)
    l.start()