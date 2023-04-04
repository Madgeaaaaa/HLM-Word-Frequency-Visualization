#import threading
#安 道 当 笑 葬花 悲 黛玉 宝玉
import B
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QWidget
from jiemian import *
from shici import *
from xuci import *
from result import *
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5,matplotli应b绘制的图可以应用在PyQt5用里面
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas#通过matplotlib.backends.backend_qt5agg类连接PyQt5

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure,self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)
        self.fig.subplots_adjust(0.2, 0.2, 0.9,0.9)
class jiemain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui=Ui_mainWindow()
        self.main_ui.setupUi(self)
class xuci(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog()
        self.child.setupUi(self)
    def showRes(self):
        words = []
        if self.child.checkBox.isChecked() == True:
            words.append(self.child.checkBox.text())
        if self.child.checkBox_2.isChecked() == True:
            words.append(self.child.checkBox_2.text())
        if self.child.checkBox_3.isChecked() == True:
            words.append(self.child.checkBox_3.text())
        if self.child.checkBox_4.isChecked() == True:
            words.append(self.child.checkBox_4.text())
        if self.child.checkBox_5.isChecked() == True:
            words.append(self.child.checkBox_5.text())
        if xuci.child.checkBox_6.isChecked() == True:
            words.append(self.child.checkBox_6.text())
        if self.child.checkBox_7.isChecked() == True:
            words.append(self.child.checkBox_7.text())
        if self.child.checkBox_8.isChecked() == True:
            words.append(self.child.checkBox_8.text())
        if self.child.checkBox_9.isChecked() == True:
            words.append(self.child.checkBox_9.text())
        if self.child.checkBox_10.isChecked() == True:
            words.append(self.child.checkBox_10.text())
        if self.child.checkBox_11.isChecked() == True:
            words.append(self.child.checkBox_11.text())
        if self.child.checkBox_12.isChecked() == True:
            words.append(self.child.checkBox_12.text())
        if self.child.checkBox_13.isChecked() == True:
            words.append(self.child.checkBox_13.text())
        if self.child.checkBox_14.isChecked() == True:
            words.append(self.child.checkBox_14.text())
        if self.child.checkBox_15.isChecked() == True:
            words.append(self.child.checkBox_15.text())
        if self.child.checkBox_16.isChecked() == True:
            words.append(self.child.checkBox_16.text())
        if self.child.checkBox_17.isChecked() == True:
            words.append(self.child.checkBox_17.text())
        if self.child.checkBox_18.isChecked() == True:
            words.append(self.child.checkBox_18.text())
        res.plot(words)
        res.show()
class shici(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child=Ui_Dialog1()
        self.child.setupUi(self)
    def showRes(self):
        text = self.child.textEdit.toPlainText()#获取文本框内容
        words = text.split(' ')
        res.plot(words)
        res.show()
class result(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.child=Ui_Form()
        self.child.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.F1 = MyFigure(width=3, height=2, dpi=100)
        self.layout1=QtWidgets.QVBoxLayout(self.child.groupBox)
        self.layout1.addWidget(self.F1)
        self.F2 = MyFigure(width=3, height=2, dpi=100)
        self.layout2 = QtWidgets.QVBoxLayout(self.child.groupBox_2)
        self.layout2.addWidget(self.F2)
    def plot(self,words):
        for i in range(self.layout1.count()):
            self.layout1.itemAt(i).widget().deleteLater()
        for i in range(self.layout2.count()):
            self.layout2.itemAt(i).widget().deleteLater()
        self.F1 = MyFigure(width=3, height=2, dpi=100)
        self.layout1.addWidget(self.F1)
        self.F2 = MyFigure(width=3, height=2, dpi=100)
        self.layout2.addWidget(self.F2)
        text = B.Gettext()
        counts = B.Getcount(text)
        counts1 = [counts[i] for i in words]
        self.F2.axes.bar(words, counts1, 0.4, color="steelblue")
        for a, b in zip(words, counts1):  # 柱子上的数字显示
            self.F2.axes.text(a, b, '%d' % b, ha='center', va='bottom', fontsize=7);
        self.F2.axes.set_ylabel("频率")
        self.F2.axes.set_xlabel("词语")
        wc = WordCloud(background_color='white',font_path='msyh.ttc',width=200,height=100)
        wordscounts = dict([(key, counts[key]) for key in words])
        wc.generate_from_frequencies(wordscounts)  # 通过频率生成词云
        self.F1.axes.imshow(wc)  # 显示词云图
        self.F1.axes.axis('off')  # 是否显示x轴、y轴下标
if __name__=='__main__':
    app=QApplication(sys.argv)
    jiemian=jiemain()
    xuci=xuci()
    shici=shici()
    res = result()
    #通过Button将两个窗体关联
    B1=jiemian.main_ui.pushButton
    B1.clicked.connect(xuci.show)
    B2=jiemian.main_ui.pushButton_2
    B2.clicked.connect(shici.show)
    B3=xuci.child.pushButton
    B3.clicked.connect(xuci.showRes)
    shici.child.pushButton_2.clicked.connect(shici.showRes)
    jiemian.show()
    sys.exit(app.exec_())


