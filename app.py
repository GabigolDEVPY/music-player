from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
import sys
sys.dont_write_bytecode = True
from main_window import MainController


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    window = MainController()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()