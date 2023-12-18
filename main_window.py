import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QPushButton, QVBoxLayout, QHBoxLayout,
                             QScrollArea, QDialog, QLineEdit, QFileDialog, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
import task_2
import task_3
import task_5
from task_1 import run1

class ScrollLabel(QScrollArea):
    """
    Creates a window for viewing reviews.

    Attributes:
    - label: QLabel widget for displaying reviews.

    Returns:
    None
    """
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        """
        Initializes the ScrollLabel.

        Args:
        - args: Positional arguments passed to the parent class.
        - kwargs: Keyword arguments passed to the parent class.

        Returns:
        None
        """
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
        """
        Sets the text of the label.

        Args:
        - text (str): The text to be displayed.

        Returns:
        None
        """
        self.label.setText(text)


class Example(QWidget):
    """
    Main application window for the lab.

    Attributes:
    - folderpath: Path to the selected folder.
    - save_folderpath: Path to the folder where the new dataset will be saved.
    - rating_iter1 to rating_iter5: Iterators for different rating categories.

    Returns:
    None
    """
    def __init__(self) -> None:
        """
        Initializes the Example class.

        Returns:
        None
        """
        super().__init__()
        self.initUI()
        self.setStyleSheet("background:#fefefe; color: #333; font-weight:bold; border-radius: 5px;")

    def initUI(self) -> None:
        """
        Initializes the UI components.

        Returns:
        None
        """
        self.showFullScreen()
        self.setWindowTitle('6212 - lab3')
        self.setWindowIcon(QIcon('home.png'))

        self.button = self.create_button('Create CSV-Dataset', self.click_csv)
        self.button_dataset = self.create_button('Create Dataset-Copy', self.click_dataset)
        self.button_dataset2 = self.create_button('Create Dataset-Copy2', self.click_dataset_copy)

        self.button_rating1 = self.create_button('1', lambda: self.get_next_review(1), 200, 50)
        self.button_rating2 = self.create_button('2', lambda: self.get_next_review(2), 200, 50)
        self.button_rating3 = self.create_button('3', lambda: self.get_next_review(3), 200, 50)
        self.button_rating4 = self.create_button('4', lambda: self.get_next_review(4), 200, 50)
        self.button_rating5 = self.create_button('5', lambda: self.get_next_review(5), 200, 50)

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
        """
        Creates and returns a QPushButton with the specified properties.

        Args:
        - text (str): The text displayed on the button.
        - slot (callable): The function to be executed when the button is clicked.
        - width (int): The minimum width of the button.
        - height (int): The minimum height of the button.

        Returns:
        QPushButton: The created button.
        """
        button = QPushButton(text, self)
        button.clicked.connect(slot)
        button.setStyleSheet(
            f"background:#007BFF; border-radius: 5px; min-width: {width}px; min-height: {height}px; color: #fff;")
        return button

    def get_next_review(self, rating: int) -> None:
        """
        Iterates reviews based on the given rating.

        Args:
        - rating (int): Rating value (1 to 5).

        Returns:
        None
        """
        rating_iter = None
        if rating == 1:
            rating_iter = self.rating_iter1
        elif rating == 2:
            rating_iter = self.rating_iter2
        elif rating == 3:
            rating_iter = self.rating_iter3
        elif rating == 4:
            rating_iter = self.rating_iter4
        elif rating == 5:
            rating_iter = self.rating_iter5

        if rating_iter is not None:
            try:
                with open(next(rating_iter), 'r', encoding='utf-8') as file:
                    self.review.setText(''.join(file.readlines()))
            except StopIteration:
                new_rating_iter = task_5.Iterator1(self.folderpath, str(rating))
                setattr(self, f'rating_iter{rating}', new_rating_iter)
                ErrorMessageBox(self, 'something went wrong')



    def click_csv(self) -> None:
        """
        Creates a window for creating a CSV file.

        Returns:
        None
        """
        dialog = QDialog(self)
        dialog.setWindowTitle('Create file CSV')
        dialog.setFixedSize(700, 300)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #0e172c')
        self.folderpath = 'Введите путь'
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setStyleSheet(
            "background:#f9f8fc; border-radius: 5px; color: #0e172c;")

        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_folder)
        browse_button.setStyleSheet("background:#0e172c; border-radius: 5px; color: #ffffff;")
        browse_button.adjustSize()

        create_button = QPushButton("Сreate CSV", dialog)
        create_button.setStyleSheet("background:#0e172c; border-radius: 5px; color: #ffffff;")
        create_button.clicked.connect(self.click_create_csv1)
        create_button.adjustSize()

        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(browse_button)
        layout.addWidget(create_button)
        dialog.setLayout(layout)

        dialog.exec_()



    def select_folder(self) -> None:
        """
        Saving the path for the folder.

        Returns:
        None
        """
        self.folderpath = (QFileDialog.getExistingDirectory(
            self, 'Select Folder'))
        self.path_line_edit.setText(self.folderpath)
        if 'dataset' in self.folderpath:
            self.rating_iter1 = task_5.Iterator1(self.folderpath, str(1))
            self.rating_iter2 = task_5.Iterator1(self.folderpath, str(2))
            self.rating_iter3 = task_5.Iterator1(self.folderpath, str(3))
            self.rating_iter4 = task_5.Iterator1(self.folderpath, str(4))
            self.rating_iter5 = task_5.Iterator1(self.folderpath, str(5))
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")

    def select_save_folder(self) -> None:
        """
        Saving the path for the folder where we will save the new dataset.

        Returns:
        None
        """
        self.save_folderpath = (QFileDialog.getExistingDirectory(self, 'Select Folder'))
        self.path_save_line_edit.setText(self.save_folderpath)

    def create_dataset_copy(self) -> None:
        """
        Сreates a folder.

        Returns:
        None
        """
        if 'dataset' in self.folderpath:
            task_2.copy_info(self.folderpath, self.save_folderpath)
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")

    def create_dataset_copy2(self) -> None:
        """
        Creates a dataset copy version 2.

        Returns:
        None
        """
        if 'dataset' in self.folderpath:
            task_3.run3(self.folderpath, self.save_folderpath)
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")

    def click_dataset(self) -> None:
        """
        Creates a window for creating a copy of the dataset.

        Returns:
        None
        """
        dialog = QDialog(self)
        dialog.setWindowTitle('Create dataset_copy')
        dialog.setFixedSize(700, 300)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #0e172c')
        self.folderpath = ''
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setStyleSheet(
            "background:#f9f8fc; border-radius: 5px; color: #0e172c;")

        self.path_save_line_edit = QLineEdit(dialog)
        self.path_save_line_edit.setEnabled(False)
        self.path_save_line_edit.setStyleSheet(
            "background:#f9f8fc; border-radius: 5px; color: #0e172c;")

        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_folder)
        browse_button.setStyleSheet("color: #ffffff; background:#0e172c; border-radius: 5px;")
        browse_button.adjustSize()

        browse_save_button = QPushButton("Browse path to save", dialog)
        browse_save_button.clicked.connect(self.select_save_folder)
        browse_save_button.setStyleSheet("color: #ffffff; background:#0e172c; border-radius: 5px;")
        browse_save_button.adjustSize()

        dataset_button = QPushButton("Сreate dataset", dialog)
        dataset_button.setStyleSheet("color: #ffffff; background:#0e172c; border-radius: 5px;")
        dataset_button.clicked.connect(self.create_dataset_copy)
        dataset_button.adjustSize()

        create_button = QPushButton("Сreate CSV", dialog)
        create_button.setStyleSheet("color: #ffffff; background:#0e172c; border-radius: 5px;")
        create_button.clicked.connect(self.click_create_csv2)
        create_button.adjustSize()

        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(self.path_save_line_edit)
        layout.addWidget(browse_save_button)
        layout.addWidget(browse_button)
        layout.addWidget(create_button)
        layout.addWidget(dataset_button)
        dialog.setLayout(layout)

        dialog.exec_()




    def click_dataset_copy(self) -> None:
        """
        Creates a window for creating a copy of the dataset copy.

        Returns:
        None
        """
        dialog = QDialog(self)
        dialog.setWindowTitle('Create dataset_copy3')
        dialog.setFixedSize(700, 300)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet('color: #0e172c')
        self.folderpath = ''
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setStyleSheet(
            "background:#f9f8fc; border-radius: 5px; color: #0e172c;")

        self.path_save_line_edit = QLineEdit(dialog)
        self.path_save_line_edit.setEnabled(False)
        self.path_save_line_edit.setStyleSheet(
            "background:#f9f8fc; border-radius: 5px; color: #0e172c;")

        browse_button = QPushButton("Browse", dialog)
        browse_button.clicked.connect(self.select_folder)
        browse_button.setStyleSheet("color: #ffffff; background:#0e172c; border-radius: 5px; color: #ffffff;")
        browse_button.adjustSize()

        browse_save_button = QPushButton("Browse path to save", dialog)
        browse_save_button.clicked.connect(self.select_save_folder)
        browse_save_button.setStyleSheet(
            "background:#0e172c; border-radius: 5px; color: #ffffff;")
        browse_save_button.adjustSize()

        dataset_button = QPushButton("Сreate dataset and CSV", dialog)
        dataset_button.setStyleSheet("color: #ffffff; background:#0e172c; border-radius: 5px; color: #ffffff;")
        dataset_button.clicked.connect(self.create_dataset_copy2)
        dataset_button.adjustSize()

        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(self.path_save_line_edit)
        layout.addWidget(browse_save_button)
        layout.addWidget(browse_button)
        layout.addWidget(dataset_button)
        dialog.setLayout(layout)

        dialog.exec_()

    def click_create_csv1(self) -> None:
        """
        A CSV file is being created.

        Returns:
        None
        """
        if 'dataset' in self.folderpath:
            run1(self.folderpath)
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")



    def click_create_csv2(self) -> None:
        """
            A csv copy file is being created

            Returns:
            None
        """
        if 'dataset' in self.folderpath:
            task_2.run2()
        else:
            ErrorMessageBox(self, "Please choose directory with dataset")


class ErrorMessageBox:
    def __init__(self, parent: QWidget, text: str) -> None:
        """
        Args:
            parent (QWidget): the main class for creating an error window
            text (str): error text

            Creates an error window

            Returns:
            None
        """
        message_box = QMessageBox(parent)
        message_box.setText(text)
        ok_button = message_box.addButton(QMessageBox.Ok)
        ok_button.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 100px;")
        message_box.setStyleSheet('color: #0e172c')
        message_box.exec_()


if __name__ == '__main__':
    """
        Сreate a base window

        Returns:
        None
    """
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
