# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1100, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("background-color: rgb(37, 39, 76);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.filters_frame = QtWidgets.QFrame(self.centralwidget)
        self.filters_frame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.filters_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filters_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filters_frame.setObjectName("filters_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.filters_frame)
        self.verticalLayout_2.setContentsMargins(50, 11, 10, 11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filter_header_ = QtWidgets.QFrame(self.filters_frame)
        self.filter_header_.setMaximumSize(QtCore.QSize(16777215, 100))
        self.filter_header_.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filter_header_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filter_header_.setObjectName("filter_header_")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.filter_header_)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.filters_text = QtWidgets.QLabel(self.filter_header_)
        self.filters_text.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.filters_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.filters_text.setObjectName("filters_text")
        self.verticalLayout_3.addWidget(self.filters_text)
        self.filter_header_line = QtWidgets.QFrame(self.filter_header_)
        self.filter_header_line.setStyleSheet("color: rgb(158, 158, 158);")
        self.filter_header_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.filter_header_line.setLineWidth(3)
        self.filter_header_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.filter_header_line.setObjectName("filter_header_line")
        self.verticalLayout_3.addWidget(self.filter_header_line)
        self.verticalLayout_2.addWidget(self.filter_header_)
        self.brands_frame = QtWidgets.QFrame(self.filters_frame)
        self.brands_frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.brands_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.brands_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.brands_frame.setObjectName("brands_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.brands_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.brands_text = QtWidgets.QLabel(self.brands_frame)
        self.brands_text.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.brands_text.setFont(font)
        self.brands_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.brands_text.setObjectName("brands_text")
        self.verticalLayout_4.addWidget(self.brands_text)
        self.sennheiser_checkbox = QtWidgets.QCheckBox(self.brands_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.sennheiser_checkbox.setFont(font)
        self.sennheiser_checkbox.setStyleSheet("color: rgb(255, 255, 255)")
        self.sennheiser_checkbox.setChecked(False)
        self.sennheiser_checkbox.setObjectName("sennheiser_checkbox")
        self.verticalLayout_4.addWidget(self.sennheiser_checkbox)
        self.jbl_checkbox = QtWidgets.QCheckBox(self.brands_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.jbl_checkbox.setFont(font)
        self.jbl_checkbox.setStyleSheet("color: rgb(255, 255, 255)")
        self.jbl_checkbox.setChecked(False)
        self.jbl_checkbox.setObjectName("jbl_checkbox")
        self.verticalLayout_4.addWidget(self.jbl_checkbox)
        self.skullcandy_checkbox = QtWidgets.QCheckBox(self.brands_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.skullcandy_checkbox.setFont(font)
        self.skullcandy_checkbox.setStyleSheet("color: rgb(255, 255, 255)")
        self.skullcandy_checkbox.setChecked(False)
        self.skullcandy_checkbox.setObjectName("skullcandy_checkbox")
        self.verticalLayout_4.addWidget(self.skullcandy_checkbox)
        self.verticalLayout_2.addWidget(self.brands_frame)
        self.search_button = QtWidgets.QPushButton(self.filters_frame)
        self.search_button.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.search_button.setFont(font)
        self.search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_button.setAcceptDrops(False)
        self.search_button.setAutoFillBackground(False)
        self.search_button.setStyleSheet("color: rgb(255, 255, 255);\n" "background-color: rgb(84, 154, 175);")
        self.search_button.setIconSize(QtCore.QSize(20, 20))
        self.search_button.setCheckable(False)
        self.search_button.setChecked(False)
        self.search_button.setAutoDefault(False)
        self.search_button.setDefault(False)
        self.search_button.setFlat(False)
        self.search_button.setObjectName("search_button")
        self.verticalLayout_2.addWidget(self.search_button)
        self.gridLayout.addWidget(self.filters_frame, 1, 0, 2, 1)
        self.header_frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QtCore.QSize(0, 100))
        self.header_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.header_frame.setAutoFillBackground(False)
        self.header_frame.setStyleSheet("background-color: rgb(69, 69, 98);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.header_frame)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_text = QtWidgets.QLabel(self.header_frame)
        self.header_text.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.header_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.header_text.setObjectName("header_text")
        self.verticalLayout.addWidget(self.header_text)
        self.gridLayout.addWidget(self.header_frame, 0, 0, 1, 2)
        self.results_frame = QtWidgets.QFrame(self.centralwidget)
        self.results_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.results_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.results_frame.setObjectName("results_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.results_frame)
        self.gridLayout_3.setContentsMargins(-1, -1, 50, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.results_table = QtWidgets.QTableWidget(self.results_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results_table.sizePolicy().hasHeightForWidth())
        self.results_table.setSizePolicy(sizePolicy)
        self.results_table.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.results_table.setFont(font)
        self.results_table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.results_table.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.results_table.setToolTipDuration(-1)
        self.results_table.setAutoFillBackground(False)
        self.results_table.setStyleSheet("")
        self.results_table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.results_table.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed
            | QtWidgets.QAbstractItemView.DoubleClicked
            | QtWidgets.QAbstractItemView.EditKeyPressed
        )
        self.results_table.setShowGrid(True)
        self.results_table.setGridStyle(QtCore.Qt.DashLine)
        self.results_table.setWordWrap(True)
        self.results_table.setCornerButtonEnabled(False)
        self.results_table.setRowCount(0)
        self.results_table.setObjectName("results_table")
        self.results_table.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(3, item)
        self.results_table.horizontalHeader().setVisible(True)
        self.results_table.horizontalHeader().setCascadingSectionResizes(False)
        self.results_table.horizontalHeader().setDefaultSectionSize(350)
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.verticalHeader().setDefaultSectionSize(50)
        self.gridLayout_3.addWidget(self.results_table, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.results_frame, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Headset Browser"))
        self.filters_text.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" font-size:22pt; font-weight:600;">Filters</span></p></body></html>',
            )
        )
        self.brands_text.setText(
            _translate("MainWindow", '<html><head/><body><p><span style=" font-weight:600;">BRANDS</span></p></body></html>')
        )
        self.sennheiser_checkbox.setText(_translate("MainWindow", "Sennheiser"))
        self.jbl_checkbox.setText(_translate("MainWindow", "JBL"))
        self.skullcandy_checkbox.setText(_translate("MainWindow", "Skullcandy"))
        self.search_button.setText(_translate("MainWindow", "SEARCH"))
        self.header_text.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p align="center"><span style=" font-size:28pt; font-weight:600;">Select at least one brand</span></p></body></html>',
            )
        )
        self.results_table.setSortingEnabled(False)
        item = self.results_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.results_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Image"))
        item = self.results_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.results_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Website"))