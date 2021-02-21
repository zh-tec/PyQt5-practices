from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys

class MyFirstApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 获取用户设备的分辨率
        # 1.获取一个桌面对象
        # 2.通过桌面对象的方法来获取桌面的宽和高
        desktop = QApplication.desktop()
        self.resize(desktop.width(), desktop.height())
        # 设置窗口标题
        self.setWindowTitle("这是第一个PyQt5应用程序")
        # 设置窗口图标
        self.setWindowIcon(QIcon('./1303152.ico'))
        # 创建一个按钮,实现关闭窗口的功能
        push_button = QPushButton("退出",self)
        # 信号和槽实现点击按钮就关闭主窗口
        push_button.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyFirstApp()
    form.show()
    # 应用程序进入主循环
    sys.exit(app.exec())