
from PyQt5.QtCore import QThread, pyqtSignal

class FeedbackController(QThread):
    def __init__(self, feedback_buffer):
        super().__init__()
        self.feedback_buffer = feedback_buffer

    def run(self):


