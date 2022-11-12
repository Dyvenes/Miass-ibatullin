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
        self.pushButton.clicked.connect(self.drawCircle)

    def drawCircle(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            r = random.randint(20, 100)
            qp.drawEllipse(QPoint(200, 200), r, r)
            qp.end()
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Chess()
    game.show()
    sys.exit(app.exec())
