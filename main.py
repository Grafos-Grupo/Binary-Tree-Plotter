import sys
from UI import QApplication, BinaryTreeApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BinaryTreeApp()
    window.show()
    sys.exit(app.exec_())


