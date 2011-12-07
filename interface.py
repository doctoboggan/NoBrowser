# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Tue Oct 25 03:21:58 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(738, 541)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.bBack = QtGui.QPushButton(self.centralwidget)
        self.bBack.setText(QtGui.QApplication.translate("MainWindow", "<=", None, QtGui.QApplication.UnicodeUTF8))
        self.bBack.setObjectName(_fromUtf8("bBack"))
        self.horizontalLayout.addWidget(self.bBack)
        self.bForward = QtGui.QPushButton(self.centralwidget)
        self.bForward.setText(QtGui.QApplication.translate("MainWindow", "=>", None, QtGui.QApplication.UnicodeUTF8))
        self.bForward.setObjectName(_fromUtf8("bForward"))
        self.horizontalLayout.addWidget(self.bForward)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.url = QtGui.QLineEdit(self.centralwidget)
        self.url.setObjectName(_fromUtf8("url"))
        self.horizontalLayout_2.addWidget(self.url)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout_2.addWidget(self.webView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.bBack, self.bForward)
        MainWindow.setTabOrder(self.bForward, self.url)
        MainWindow.setTabOrder(self.url, self.webView)

    def retranslateUi(self, MainWindow):
        pass

from PyQt4 import QtWebKit
