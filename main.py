from pygame import *
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Выберете игру:')
button = QPushButton('Прятки')
button_2 = QPushButton("Пинг-понг")
text = QLabel('Выберете игру:')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
line.addWidget(button_2, alignment = Qt.AlignCenter)
main_win.setLayout(line)

#button.clicked.connect(main_2)

main_win.show()
app.exec_()