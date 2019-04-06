import sys
from PyQt5 import QtWidgets

from View.main_window import MainWindow
from Controller.main_cont import MainController

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_ctr = MainController()
    mainWin = MainWindow(main_ctr)
    mainWin.show()

    ret = app.exec_()

    main_ctr.crawler.stop()
    main_ctr.tc.kill_all()
    sys.exit(ret)

