

from PyQt5.QtCore import QThread, pyqtSignal
import threading
from queue import Queue
import time

class FeedbackController(threading.Thread, QThread):
    def __init__(self, q, cond:threading.Condition):
        threading.Thread.__init__(self)
        QThread.__init__(self)
        self.q = q
        self.cond = cond
        print("init feedback")

    def run(self):
        print("feedback")
        with self.cond:
            while True:

                print("feed while")
                self.cond.wait()
                print(q.get())
                self.cond.notify()




class LDA(QThread):
    def __init__(self, q, cond:threading.Condition):
        super().__init__()
        self.q = q
        self.cond = cond
        print("init lda")

    def run(self):
        print("lda")


        with self.cond:
            while True:
                print("lda while")
                time.sleep(10)
                q.put(3)
                self.cond.notify()
                self.cond.wait()


q = Queue()
if __name__ == '__main__':

    cond = threading.Condition()
    f = FeedbackController(q, cond)
    f.start()
    l = LDA(q,cond)

    l.start()