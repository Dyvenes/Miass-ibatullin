import sys

from PyQt5.QtWidgets import QApplication, QWidget


class Chess(QWidget, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Chess()
    game.show()
    sys.exit(app.exec())
