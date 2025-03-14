# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(755, 550)
        MainWindow.setMaximumSize(QSize(762, 550))
        MainWindow.setStyleSheet(u"QLabel {\n"
"  \n"
"	font: 700 9pt \"Microsoft PhagsPa\";\n"
"\n"
"}\n"
"\n"
"QFrame {\n"
"	\n"
"	background-color: rgb(94, 101, 107);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    border: 1px solid gray;\n"
"    border-radius: 40px; /* K\u00f6\u015fe yuvarlakl\u0131\u011f\u0131 */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_12 = QFrame(self.frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/main/db.png"))

        self.verticalLayout_8.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.frame_13)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_9.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_13)


        self.verticalLayout.addWidget(self.frame_12)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(666, 437))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(15, -1, 9, -1)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(40,5)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(16777214, 16777215))
        self.tableWidget.setStyleSheet(u"border-radius: 30px;")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.horizontalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(630, 204))
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(303, 186))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.comboBox = QComboBox(self.frame_10)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_4.addWidget(self.comboBox)

        self.pushButton_3 = QPushButton(self.frame_10)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_4.addWidget(self.pushButton_3)


        self.horizontalLayout_5.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_5.addWidget(self.pushButton_2)


        self.horizontalLayout_6.addWidget(self.frame_11)


        self.horizontalLayout_5.addWidget(self.frame_9, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_7.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_4.addWidget(self.frame_7, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GENEL BARKOD S\u0130STEM\u0130", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Genel Barkod Sistemi", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Se\u00e7", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Yazd\u0131r", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Temizle", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u00d6ncelikle barkodlar\u0131 se\u00e7melisiniz", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ard\u0131ndan yaz\u0131c\u0131y\u0131 se\u00e7melisiniz se\u00e7tikten sonra se\u00e7 butonuna t\u0131klamal\u0131s\u0131n\u0131z", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Yazd\u0131r butonuna t\u0131klad\u0131ktan sonra yazd\u0131r\u0131lacakt\u0131r", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Temizle butonuna t\u0131klad\u0131ktan sonra se\u00e7ilen barkodlar temizlenecektir :)", None))
    # retranslateUi

