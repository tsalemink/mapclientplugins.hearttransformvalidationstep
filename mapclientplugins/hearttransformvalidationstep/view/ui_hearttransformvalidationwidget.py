# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt\hearttransformvalidationwidget.ui'
#
# Created: Sun Mar  3 19:08:16 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_HeartTransformValidationWidget(object):
    def setupUi(self, HeartTransformValidationWidget):
        HeartTransformValidationWidget.setObjectName("HeartTransformValidationWidget")
        HeartTransformValidationWidget.resize(848, 386)
        self.horizontalLayout = QtGui.QHBoxLayout(HeartTransformValidationWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.control_widget = QtGui.QWidget(HeartTransformValidationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_widget.sizePolicy().hasHeightForWidth())
        self.control_widget.setSizePolicy(sizePolicy)
        self.control_widget.setObjectName("control_widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.control_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.continue_push_button = QtGui.QPushButton(self.control_widget)
        self.continue_push_button.setObjectName("continue_push_button")
        self.horizontalLayout_2.addWidget(self.continue_push_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.control_widget)
        self.display_widget = QtGui.QWidget(HeartTransformValidationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_widget.sizePolicy().hasHeightForWidth())
        self.display_widget.setSizePolicy(sizePolicy)
        self.display_widget.setObjectName("display_widget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.display_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(20, 47, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.rms_display_label = QtGui.QLabel(self.display_widget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.rms_display_label.setFont(font)
        self.rms_display_label.setObjectName("rms_display_label")
        self.horizontalLayout_3.addWidget(self.rms_display_label)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtGui.QSpacerItem(20, 47, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.validation_result_label = QtGui.QLabel(self.display_widget)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.validation_result_label.setFont(font)
        self.validation_result_label.setObjectName("validation_result_label")
        self.horizontalLayout_4.addWidget(self.validation_result_label)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtGui.QSpacerItem(20, 47, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)
        self.horizontalLayout.addWidget(self.display_widget)

        self.retranslateUi(HeartTransformValidationWidget)
        QtCore.QMetaObject.connectSlotsByName(HeartTransformValidationWidget)

    def retranslateUi(self, HeartTransformValidationWidget):
        HeartTransformValidationWidget.setWindowTitle(QtGui.QApplication.translate("HeartTransformValidationWidget", "Heart Transform Validation", None, QtGui.QApplication.UnicodeUTF8))
        self.continue_push_button.setText(QtGui.QApplication.translate("HeartTransformValidationWidget", "Continue", None, QtGui.QApplication.UnicodeUTF8))
        self.rms_display_label.setText(QtGui.QApplication.translate("HeartTransformValidationWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.validation_result_label.setText(QtGui.QApplication.translate("HeartTransformValidationWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

