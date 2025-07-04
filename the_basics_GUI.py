import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI")
        self.setGeometry(350,225,900,520)
        self.setWindowIcon(QIcon("D:/MyProjects/practice/GUI/gui_image"))

def main():
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__" :
    main()


