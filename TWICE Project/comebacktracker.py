import sys
from tracking_timer import UiForm
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UiForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
