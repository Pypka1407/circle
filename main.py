import sys
import random

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtGui import QPainter, QColor


class MyWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.diameter = 0

    def run(self):
        self.diameter = random.randint(50, 200)
        self.update()

    def paintEvent(self, event):
        if self.diameter > 0:
            painter = QPainter(self)
            painter.setBrush(QColor(255, 255, 0))
            center_x = (self.width() - self.diameter) // 2
            center_y = (self.height() - self.diameter) // 2
            painter.drawEllipse(center_x, center_y, self.diameter, self.diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())



