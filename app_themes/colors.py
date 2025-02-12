from PyQt6.QtWidgets import (
    QTabBar,
    QApplication,
    QMainWindow,
    QPushButton,
    QColorDialog,
    QMessageBox,
    QWidget,
    QLabel,
    QVBoxLayout,
    QTextEdit,
    QLayout,
    QLabel,
    QHBoxLayout
)
from PyQt6.QtGui import QColor, QIcon, QColor
from PyQt6.QtCore import Qt
import sys


class Colors(QMainWindow):
    def __init__(self):
        super().__init__()

    def apply_sky_blue_theme(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #87CEEB; /* Sky blue background */
            }
            QToolBar {
                background-color: #4682B4; /* Steel blue */
            }
            QToolButton {
                color: white;
                font-size: 14px;
            }
        """)           
