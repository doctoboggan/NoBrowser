#!/usr/bin/python -d
 
import sys
from PyQt4 import QtCore, QtGui
from interface import Ui_MainWindow
 
class NoBrowser(QtGui.QMainWindow):

  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    self.initUI()
    
  def initUI(self):
    self.connect(self.ui.bBack, QtCore.SIGNAL('clicked()'), self.ui.webView.back)
    self.connect(self.ui.bForward, QtCore.SIGNAL('clicked()'), self.ui.webView.forward)
    self.connect(self.ui.url, QtCore.SIGNAL('returnPressed()'), self.browse)

  def browse(self):
    url = self.ui.url.text() if self.ui.url.text() else self.default_url
    print url
    self.ui.webView.load(QtCore.QUrl(url))
    self.ui.webView.show()

  def mousePressEvent(self, event):
    self.offset = event.pos()

  def mouseMoveEvent(self, event):
    x=event.globalX()
    y=event.globalY()
    x_w = self.offset.x()
    y_w = self.offset.y()
    self.move(x-x_w, y-y_w)
    
 
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = NoBrowser()
  myapp.show()
  sys.exit(app.exec_())
