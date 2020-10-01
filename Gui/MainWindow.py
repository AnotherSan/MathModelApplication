from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QComboBox, QDialog, QGridLayout, \
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QSizePolicy, QTableWidget, QVBoxLayout


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)


        self.create_top_left_group_box()
        self.create_top_right_group_box()


        main_layout = QGridLayout()
        main_layout.addWidget(self.top_left_group_box, 1, 0,2,1)
        main_layout.addWidget(self.top_right_group_box, 3, 0)
        main_layout.setRowStretch(1, 1)
        main_layout.setRowStretch(2, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
        self.setLayout(main_layout)

        self.setWindowTitle("Математическая модель")
        self.setMinimumSize(800, 600)
        self.setWindowIcon(QIcon(r'Images\presentation.png'))
        self.setWindowFlags(self.windowFlags()
                            | QtCore.Qt.WindowMinimizeButtonHint
                            | QtCore.Qt.WindowMaximizeButtonHint)

    def create_top_left_group_box(self):
        self.top_left_group_box = QGroupBox("Ввод данных")

        name_str = QLabel()
        name_str.setText("Начальная скорость:")
        self.save_name_input = QLineEdit()
        self.save_name_input.setPlaceholderText("V")
        name_str_form = QLabel()
        name_str_form.setText("Угол:")
        self.format_input = QLineEdit()
        self.format_input.setPlaceholderText("Угол")
        coordinate_str=QLabel()
        coordinate_str.setText("Начальная координата:")
        self.coordinate_input=QLineEdit()
        self.coordinate_input.setPlaceholderText("x0")

        button_save = QPushButton("Ввести данные")
        layout = QVBoxLayout()
        layout.addWidget(name_str)
        layout.addWidget(self.save_name_input)
        layout.addWidget(name_str_form)
        layout.addWidget(self.format_input)
        layout.addWidget(coordinate_str)
        layout.addWidget(self.coordinate_input)
        layout.addWidget(button_save)
        layout.addStretch(1)
        self.top_left_group_box.setLayout(layout)

    def create_top_right_group_box(self):
        self.top_right_group_box = QGroupBox()

        default_push_button = QPushButton("Помощь")


        layout = QVBoxLayout()
        layout.addWidget(default_push_button)
        layout.addStretch(1)
        self.top_right_group_box.setLayout(layout)


