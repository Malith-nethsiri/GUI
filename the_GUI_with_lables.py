import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(350,225,900,520)
        self.setWindowIcon(QIcon("D:/MyProjects/practice/GUI/gui_image"))
        self.lables()

    def lables(self):
        topic = QLabel("topic of the window", self)
        topic.setFont(QFont("Verdana",40))
        #topic.move(50,50)
        topic.adjustSize()
        topic.setStyleSheet("color:red; ")


def main():
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__" :
    main()


