import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QPushButton, QVBoxLayout, QHBoxLayout,
                             QScrollArea, QDialog, QLineEdit, QFileDialog)
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor
from PyQt5.QtCore import Qt


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


class Example(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.setStyleSheet("background:#fefefe; color: #333; font-weight:bold; border-radius: 5px;")

    def initUI(self) -> None:
        self.setWindowTitle('6212 - lab3')
        self.setWindowIcon(QIcon('home.png'))

        self.button = self.create_button('Create CSV-Dataset', self.click_csv)
        self.button_dataset = self.create_button('Create Dataset-Copy', self.click_dataset)
        self.button_dataset2 = self.create_button('Create Dataset-Copy2', self.click_dataset_copy)

        self.button_rating1 = self.create_button('1', self.get_next_review_1, 200, 50)
        self.button_rating2 = self.create_button('2', self.get_next_review_2, 200, 50)
        self.button_rating3 = self.create_button('3', self.get_next_review_3, 200, 50)
        self.button_rating4 = self.create_button('4', self.get_next_review_4, 200, 50)
        self.button_rating5 = self.create_button('5', self.get_next_review_5, 200, 50)

        self.review = ScrollLabel(self)
        self.review.setStyleSheet("background:#DFDFDF; color: #0e172c; border-radius: 5px;")

        main_layout = QVBoxLayout(self)

        main_buttons_layout = QHBoxLayout()
        main_buttons_layout.addWidget(self.button_dataset)
        main_buttons_layout.addWidget(self.button)
        main_buttons_layout.addWidget(self.button_dataset2)

        rating_layout = QHBoxLayout()
        rating_layout.addWidget(self.button_rating1)
        rating_layout.addWidget(self.button_rating2)
        rating_layout.addWidget(self.button_rating3)
        rating_layout.addWidget(self.button_rating4)
        rating_layout.addWidget(self.button_rating5)

        main_layout.addLayout(main_buttons_layout)
        main_layout.addLayout(rating_layout)
        main_layout.addWidget(self.review)

        self.show()

    def create_button(self, text, slot, width=200, height=50):
        button = QPushButton(text, self)
        button.clicked.connect(slot)
        button.setStyleSheet(
            f"background:#007BFF; border-radius: 5px; min-width: {width}px; min-height: {height}px; color: #fff;")
        return button

    def get_next_review_1(self) -> None:
        pass

    def get_next_review_2(self) -> None:
        pass

    def get_next_review_3(self) -> None:
        pass

    def get_next_review_4(self) -> None:
        pass

    def get_next_review_5(self) -> None:
        pass

    def click_csv(self) -> None:
        pass

    def click_dataset(self) -> None:
        pass

    def click_dataset_copy(self) -> None:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
