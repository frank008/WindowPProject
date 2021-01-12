import pyautogui
import time
from PyQt5 import QtWidgets
from main.src import JianShe
import sys
import   threading as th

import tkinter
import tkinter.messagebox#弹窗库



class MyPyQT_Form(QtWidgets.QWidget, JianShe.Ui_Form):
    def __init__(self):
        super().__init__()
        super(JianShe.Ui_Form, self).__init__()
        self.setupUi(self)
        self.stopFlag=""
        self.isStart=0




    def startClick(self):
        th.Thread(target=self.clickWin,args=("A",)).start()


    def clickExec(self):
        self.stopFlag="stop"
        sys.exit(0)

    def clickWin(self,B):
        if(self.isStart==0):
            root = tkinter.Tk()
            root.withdraw()
            tkinter.messagebox.showinfo(title='状态', message='启动中...！')
            root.destroy()
        else:
            root = tkinter.Tk()
            root.withdraw()
            tkinter.messagebox.showwarning(title='状态', message='已启动.....！')
            root.destroy()
            return
        self.isStart = 1
        while (True):
            if (self.stopFlag == "stop"):
                break
            time.sleep(5)
            pyautogui.click()

if __name__ == '__main__':
    flag=0
    if(flag==0):
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showinfo(title='状态', message='程序正在启动.....！')
        root.destroy()
        flag = 1
        app = QtWidgets.QApplication(sys.argv)
        my_pyqt_form = MyPyQT_Form()
        my_pyqt_form.show()
        sys.exit(app.exec_())







