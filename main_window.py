import sys
from PyQt5.QtWidgets import (
    QMessageBox, QFileDialog, QWidget, QLabel, QApplication, QPushButton,
    QToolTip, QVBoxLayout, QScrollArea, QDialog, QLineEdit
)
from PyQt5.QtGui import QFont, QIcon


class ScrollLabel(QScrollArea):
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        text = QWidget(self)
        self.setWidget(text)
        lay = QVBoxLayout(text)
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)
        self.label.setFont(QFont("SansSerif", 18))

    def setText(self, text: str) -> None:
        self.label.setText(text)


class ErrorMessageBox:
    def __init__(self, parent: QWidget, text: str) -> None:
        message_box = QMessageBox(parent)
        message_box.setText(text)
        ok_button = message_box.addButton(QMessageBox.Ok)
        ok_button.setStyleSheet(
            "background:#007BFF; border-radius: 5px; min-width: 100px; color: #fff;")
        message_box.setStyleSheet('color: #333;')
        message_box.exec_()


class Example(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.setStyleSheet(
            "background:#fefefe; color: #333; font-weight:bold; border-radius: 5px;")

    def initUI(self) -> None:
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle('LAB_3')
        self.setWindowIcon(QIcon('home.png'))

        self.button = QPushButton('Create CSV-Dataset', self)
        self.button.clicked.connect(self.click_csv)  # Placeholder, replace with actual function
        self.button.setStyleSheet(
            "background:#007BFF; border-radius: 5px; min-width: 200px; min-height: 50px; color: #fff;")

        self.button_dataset = QPushButton('Create Dataset-Copy', self)
        self.button_dataset.clicked.connect(self.click_dataset)
        self.button_dataset.setStyleSheet(
            "background:#007BFF; border-radius: 5px; min-width: 200px; min-height: 50px; color: #fff;")

        self.review = ScrollLabel(self)
        self.review.setStyleSheet(
            "background:#d9d4e7; color: #0e172c; border-radius: 5px;")

        layout = QVBoxLayout(self)

        layout.addWidget(self.button_dataset)
        layout.addWidget(self.button)
        layout.addWidget(self.review)

    def click_csv(self):
        print("Create CSV-Dataset")

    def click_dataset(self):
        print("Create Dataset-Copy")


def application() -> None:
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
