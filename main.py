import random
import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from ui import Ui_Form


class Chess(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.yellow = False
        self.pushButton.clicked.connect(self.YellowCircle)
        self.pushButton_2.clicked.connect(self.RandomCircle)

    def YellowCircle(self):
        self.do_paint = True
        self.yellow = True
        self.repaint()

    def RandomCircle(self):
        self.do_paint = True
        self.yellow = False
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            if self.yellow:
                color = QColor('yellow')
            else:
                color = QColor(random.randint(0, 0xffffff))
            qp.setBrush(QColor(color))
            r = random.randint(20, 100)
            w = self.width()
            h = self.height()
            qp.drawEllipse(QPoint(random.randint(r, w - r),
                                  random.randint(r, h - r)), r, r)
            qp.end()
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Chess()
    game.show()
    sys.exit(app.exec())
