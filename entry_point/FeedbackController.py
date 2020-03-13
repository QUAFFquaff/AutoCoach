import threading
from PyQt5.QtCore import QThread, pyqtSignal
from queue import Queue


class FeedbackController(threading.Thread, QThread):

    feedback_signal = pyqtSignal([int])

    def __init__(self, pattern_queue: Queue, cond:threading.Condition):
        threading.Thread.__init__(self)
        QThread.__init__(self)
        self.pattern_queue = pattern_queue
        self.cond = cond
        print("init feedback")

    def run(self):
        with self.cond:
            print("feedback")
            while True:
                feedback_queue = Queue()
                self.cond.wait()
                while not self.pattern_queue.empty():
                    feedback_queue.put(self.pattern_queue.get())
                self.cond.notify()

                # deal with feedback




