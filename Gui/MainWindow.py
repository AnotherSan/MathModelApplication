from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import QComboBox, QDialog, QGridLayout, \
    QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QSizePolicy, QTableWidget, QVBoxLayout, QGraphicsLayout, QHeaderView, QTableWidgetItem
import numpy as np
import pyqtgraph as pg
import matplotlib.pylab as plot
import math as m
from math import tan, pi, cos, sin
import sqlite3


class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.create_top_left_group_box()
        self.create_table_widget()
        self.create_bottom_left_tab_widget()

        main_layout = QGridLayout()
        main_layout.addWidget(self.bottom_left_tab_widget, 1, 1, 3, 3)
        main_layout.addWidget(self.top_left_group_box, 1, 0, 1, 1)
        main_layout.addWidget(self.botton_table_widget, 2, 0, 2, 1)
        main_layout.setRowStretch(1, 1)
        main_layout.setRowStretch(2, 1)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
        self.setLayout(main_layout)

        self.setWindowTitle("Математическая модель движения мяча под углом к горизонту")
        self.setMinimumSize(800, 600)
        self.setWindowIcon(QIcon(r'Images\presentation.png'))
        self.setWindowFlags(self.windowFlags()
                            | QtCore.Qt.WindowMinimizeButtonHint
                            | QtCore.Qt.WindowMaximizeButtonHint)

    def create_bottom_left_tab_widget(self):
        self.bottom_left_tab_widget = QGroupBox("Траектория мяча")
        self.dynamicPlt = pg.PlotWidget()
        self.dynamicPlt.setLabel('left', 'Y')
        self.dynamicPlt.setLabel('bottom', 'X')
        self.dynamicPlt.showGrid(x=True, y=True)
        graphic_h_box = QHBoxLayout()
        graphic_h_box.addWidget(self.dynamicPlt)
        self.bottom_left_tab_widget.setLayout(graphic_h_box)

    # def timerForGraphic(self):
    #    self.timer2 = pg.QtCore.QTimer()
    #    self.timer2.timeout.connect(self.update)
    #    self.timer2.setInterval(1000)
    #   self.timer2.start()
    def create_table_widget(self):
        self.botton_table_widget = QGroupBox("Таблица вывода данных")
        self.table_widget = QTableWidget()
        self.table_widget.setAlternatingRowColors(True)
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setCascadingSectionResizes(True)
        self.table_widget.horizontalHeader().setSortIndicatorShown(False)
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().Stretch
        self.table_widget.horizontalHeader().ResizeToContents
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_widget.verticalHeader().Stretch
        self.table_widget.verticalHeader().ResizeToContents
        self.table_widget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_widget.verticalHeader().setVisible(True)
        self.table_widget.verticalHeader().setCascadingSectionResizes(True)
        self.table_widget.verticalHeader().setStretchLastSection(False)
        self.table_widget.setHorizontalHeaderLabels(("X (м)", "Y (м)", "t (с)"))
        table_h_box = QHBoxLayout()
        table_h_box.addWidget(self.table_widget)
        self.botton_table_widget.setLayout(table_h_box)

    def update(self):
        v = int(self.speed_input.text())  # начальная скорость (м/с)
        g = 9.8  # ускорение свободного падения (м/с**2)
        angle = int(self.angle_input.text())  # начальный угол
        y0 = int(self.coordinate_input.text())  # начальная вертикальная координата
        rad = 180 / pi
        angle1 = angle / rad
        t = np.linspace(0, 5, num=100)
        x1 = []
        y1 = []
        if 5 <= angle <= 175 and v > 0:
            for k in t:
                x = ((v * k) * np.cos(angle1))
                y = ((v * k) * np.sin(angle1)) - ((0.5 * g) * (k ** 2)) + y0
                t = (2 * v * np.sin(angle1)) / g  # время движения брошенного тела
                if y > 0:
                    self.conn = sqlite3.connect("coordinateBase.db")
                    self.c = self.conn.cursor()
                    self.c.execute("INSERT INTO Coordinate (X,Y,t) VALUES (?,?,?)", (x, y, t))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                x1.append(x)
                y1.append(y)
            p = [i for i, j in enumerate(y1) if j < 0]
            for i in sorted(p, reverse=True):
                del x1[i]
                del y1[i]
            pen = pg.mkPen(color=(255, 0, 0), width=1, style=QtCore.Qt.DashLine)
            self.dynamicPlt.plot(x1, y1, pen=pen, symbol='o', symbolBrush='b')
            self.load_data()

    def deleteGraphics(self):
        self.conn = sqlite3.connect("coordinateBase.db")
        self.c = self.conn.cursor()
        self.c.execute("DELETE from Coordinate")
        self.conn.commit()
        self.c.close()
        self.conn.close()
        self.load_data()
        plotItem = self.dynamicPlt.getPlotItem()
        plotItem.clear()

    def create_top_left_group_box(self):
        self.top_left_group_box = QGroupBox("Ввод данных")
        self.onlyInt = QIntValidator()
        name_str = QLabel()
        name_str.setText("Начальная скорость:")
        self.speed_input = QLineEdit()
        self.speed_input.setPlaceholderText("V (м/с) V>0")
        self.speed_input.setValidator(self.onlyInt)
        name_str_form = QLabel()
        name_str_form.setText("Угол:")
        self.angle_input = QLineEdit()
        self.angle_input.setPlaceholderText("Градусы 5<=angle<=175")
        self.angle_input.setValidator(self.onlyInt)
        coordinate_str = QLabel()
        coordinate_str.setText("Начальная координата:")
        self.coordinate_input = QLineEdit()
        self.coordinate_input.setPlaceholderText("y0 (м)")
        self.coordinate_input.setValidator(self.onlyInt)

        button_input = QPushButton("Ввести данные")
        button_input.clicked.connect(self.update)
        button_delete = QPushButton("Удалить графики")
        button_delete.clicked.connect(self.deleteGraphics)

        layout = QVBoxLayout()
        layout.addWidget(name_str)
        layout.addWidget(self.speed_input)
        layout.addWidget(name_str_form)
        layout.addWidget(self.angle_input)
        layout.addWidget(coordinate_str)
        layout.addWidget(self.coordinate_input)
        layout.addWidget(button_input)
        layout.addWidget(button_delete)
        layout.addStretch(1)
        self.top_left_group_box.setLayout(layout)

    def load_data(self):
        self.connect_ = sqlite3.connect(r'coordinateBase.db')
        _result = self.connect_.execute("SELECT * FROM Coordinate")
        self.table_widget.setRowCount(0)
        for row_number, row_data in enumerate(_result):
            self.table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table_widget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connect_.close()
