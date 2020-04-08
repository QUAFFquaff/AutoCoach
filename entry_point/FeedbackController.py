import threading
from PyQt5.QtCore import QThread, pyqtSignal
from queue import Queue

personlaity = 3
threshold = {0: [40, 60], 1:[40, 70], 2:[50, 70], 3:[40, 85]}  #threshold for feedback

class FeedbackController(threading.Thread, QThread):

    feedback_signal = pyqtSignal(int, str)

    def __init__(self, pattern_queue: Queue, cond:threading.Condition):
        threading.Thread.__init__(self)
        QThread.__init__(self)
        self.pattern_queue = pattern_queue
        self.cond = cond
        print("init feedback")

    def run(self):
        with self.cond:
            while True:
                feedback_queue = []
                self.cond.wait()
                while not self.pattern_queue.empty():
                    feedback_queue.append(self.pattern_queue.get())
                self.cond.notify()

                # deal with feedback
                event_mid_dict = {'i':0, 'b':0, 'p':0, 'w':0}
                event_high_dict = {'j':0, 'c':0, 'q':0, 'x':0}
                sum_score = 0
                avg_score = 0
                for feedbackPack in feedback_queue:
                    patterns = feedbackPack[0]
                    score = feedbackPack[1]

                    print("pattern:"+patterns)
                    print("score"+str(score))
                    sum_score+=score
                    for pattern in patterns:
                        if pattern in event_mid_dict:
                            event_mid_dict[pattern]+=1
                    for pattern in patterns:
                        if pattern in event_high_dict:
                            event_high_dict[pattern] += 1

                print(event_high_dict)
                avg_score = sum_score / len(feedback_queue)
                if personlaity == 3:
                    if avg_score in range(threshold[personlaity][0], threshold[personlaity][1]):  # need feedback
                        max_high = max(event_high_dict, key=event_high_dict.get)
                        max_mid = max(event_mid_dict, key=event_mid_dict.get)
                        print("dapzhelema")
                        if event_high_dict[max_high] != 0:
                            self.feedback_signal.emit(2, self.transfer(max_high))
                        elif event_mid_dict[max_mid] != 0:
                            self.feedback_signal.emit(1, self.transfer(max_mid))
                        else:
                            print("到这里了吗")
                            self.feedback_signal.emit(0, 'no')


    def transfer(self, event: str):
        if event == 'b' or event == 'c':
            return 'acc'
        if event == 'i' or event == 'j':
            return 'brake'
        if event == 'p' or event == 'q':
            return 'turn'
        if event == 'w' or event == 'x':
            return 'swerve'

