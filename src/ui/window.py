# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Window(object):
    def setupUi(self, Window):
        if Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(456, 175)
        self.centralwidget = QWidget(Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_name = QLabel(self.centralwidget)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setGeometry(QRect(40, 10, 231, 31))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 60, 311, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_previous = QPushButton(self.horizontalLayoutWidget)
        self.btn_previous.setObjectName(u"btn_previous")

        self.horizontalLayout.addWidget(self.btn_previous)

        self.btn_playpause = QPushButton(self.horizontalLayoutWidget)
        self.btn_playpause.setObjectName(u"btn_playpause")

        self.horizontalLayout.addWidget(self.btn_playpause)

        self.btn_next = QPushButton(self.horizontalLayoutWidget)
        self.btn_next.setObjectName(u"btn_next")

        self.horizontalLayout.addWidget(self.btn_next)

        self.lbl_state = QLabel(self.centralwidget)
        self.lbl_state.setObjectName(u"lbl_state")
        self.lbl_state.setGeometry(QRect(310, 10, 131, 41))
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"MainWindow", None))
        self.lbl_name.setText(QCoreApplication.translate("Window", u"Name", None))
        self.btn_previous.setText(QCoreApplication.translate("Window", u"Previous", None))
        self.btn_playpause.setText(QCoreApplication.translate("Window", u"Play/Pause", None))
        self.btn_next.setText(QCoreApplication.translate("Window", u"Next", None))
        self.lbl_state.setText(QCoreApplication.translate("Window", u"ETAT", None))
    # retranslateUi

