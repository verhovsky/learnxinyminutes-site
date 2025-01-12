import sys
from PyQt4 import QtGui

def window():
    # 创建应用对象
    app = QtGui.QApplication(sys.argv)
    # 创建一个 widget，作为 label 的父控件
    w = QtGui.QWidget()
    # 在 widget 中添加一个 label 子控件
    b = QtGui.QLabel(w)
    # 设置 label 的文字
    b.setText("Hello World!")
    # 设置 widget 的尺寸和位置
    w.setGeometry(100, 100, 200, 50)
    b.move(50, 20)
    # 设置窗口的标题
    w.setWindowTitle("PyQt")
    # 显示 widget 及其所有子控件
    w.show()
    # 下面让程序跑起来，这行代码会启动事件循环并阻塞直到应用程序退出。
    sys.exit(app.exec_())
if __name__ == '__main__':
    window()
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
def window():
    app = QApplication(sys.argv)
    w = QWidget()
    # 创建一个按钮并添加到 widget 控件 w
    b = QPushButton(w)
    b.setText("Press me")
    b.move(50, 50)
    # 当按钮 b 被点击时调用 showdialog 函数
    # 注意函数调用时没有“()”，这样函数就能以对象的方式传入而非传入执行它所得到的返回值
    # 更多关于 pyqt 函数调用、传参等的内容见 pyqt 的信号机制
    b.clicked.connect(showdialog)
    w.setWindowTitle("PyQt Dialog")
    w.show()
    sys.exit(app.exec_())

# 对话框窗口创建函数
# 当窗口中的按钮被点击时退出本程序
def showdialog():
    d = QDialog()
    b1 = QPushButton("ok", d)
    b1.move(50, 50)
    d.setWindowTitle("Dialog")
    # 这里的模态实现了在对话框弹出时阻塞程序同时屏蔽父窗口
    d.setWindowModality(Qt.ApplicationModal)
    # 当按钮被点击时整个进程将会结束
    b1.clicked.connect(sys.exit)
    d.exec_()
if __name__ == '__main__':
    window()
