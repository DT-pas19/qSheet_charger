# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vexillum.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(678, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_comment = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_comment.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_comment.setText("")
        self.edit_comment.setObjectName("edit_comment")
        self.gridLayout.addWidget(self.edit_comment, 4, 1, 1, 3)
        self.lbl_date = QtWidgets.QLabel(self.centralwidget)
        self.lbl_date.setObjectName("lbl_date")
        self.gridLayout.addWidget(self.lbl_date, 2, 0, 1, 1)
        self.lbl_disknumber = QtWidgets.QLabel(self.centralwidget)
        self.lbl_disknumber.setObjectName("lbl_disknumber")
        self.gridLayout.addWidget(self.lbl_disknumber, 2, 2, 1, 1)
        self.lbl_artist = QtWidgets.QLabel(self.centralwidget)
        self.lbl_artist.setObjectName("lbl_artist")
        self.gridLayout.addWidget(self.lbl_artist, 0, 0, 1, 1)
        self.edit_disknumber = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_disknumber.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edit_disknumber.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_disknumber.setText("")
        self.edit_disknumber.setObjectName("edit_disknumber")
        self.gridLayout.addWidget(self.edit_disknumber, 2, 3, 1, 1)
        self.lbl_filename = QtWidgets.QLabel(self.centralwidget)
        self.lbl_filename.setObjectName("lbl_filename")
        self.gridLayout.addWidget(self.lbl_filename, 6, 0, 1, 1)
        self.lbl_comment = QtWidgets.QLabel(self.centralwidget)
        self.lbl_comment.setObjectName("lbl_comment")
        self.gridLayout.addWidget(self.lbl_comment, 4, 0, 1, 1)
        self.edit_artist = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_artist.setObjectName("edit_artist")
        self.gridLayout.addWidget(self.edit_artist, 0, 1, 1, 3)
        self.btn_filedialog = QtWidgets.QPushButton(self.centralwidget)
        self.btn_filedialog.setMaximumSize(QtCore.QSize(30, 16777215))
        self.btn_filedialog.setObjectName("btn_filedialog")
        self.gridLayout.addWidget(self.btn_filedialog, 6, 5, 1, 1)
        self.edit_album = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_album.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_album.setText("")
        self.edit_album.setObjectName("edit_album")
        self.gridLayout.addWidget(self.edit_album, 1, 1, 1, 3)
        self.edit_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_filename.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_filename.setText("")
        self.edit_filename.setObjectName("edit_filename")
        self.gridLayout.addWidget(self.edit_filename, 6, 1, 1, 4)
        self.edit_date = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_date.setMaximumSize(QtCore.QSize(130, 16777215))
        self.edit_date.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edit_date.setText("")
        self.edit_date.setObjectName("edit_date")
        self.gridLayout.addWidget(self.edit_date, 2, 1, 1, 1)
        self.lbl_album = QtWidgets.QLabel(self.centralwidget)
        self.lbl_album.setObjectName("lbl_album")
        self.gridLayout.addWidget(self.lbl_album, 1, 0, 1, 1)
        self.tab_tracks = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_tracks.setObjectName("tab_tracks")
        self.tab_parse = QtWidgets.QWidget()
        self.tab_parse.setAccessibleName("")
        self.tab_parse.setObjectName("tab_parse")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_parse)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_pattern = QtWidgets.QLabel(self.tab_parse)
        self.lbl_pattern.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lbl_pattern.setObjectName("lbl_pattern")
        self.gridLayout_2.addWidget(self.lbl_pattern, 0, 0, 1, 1)
        self.edit_trackdata = QtWidgets.QPlainTextEdit(self.tab_parse)
        self.edit_trackdata.setObjectName("edit_trackdata")
        self.gridLayout_2.addWidget(self.edit_trackdata, 1, 0, 2, 2)
        self.btn_next_1 = QtWidgets.QPushButton(self.tab_parse)
        self.btn_next_1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_next_1.setObjectName("btn_next_1")
        self.gridLayout_2.addWidget(self.btn_next_1, 2, 2, 1, 1)
        self.box_pattern = QtWidgets.QComboBox(self.tab_parse)
        self.box_pattern.setEditable(True)
        self.box_pattern.setObjectName("box_pattern")
        self.gridLayout_2.addWidget(self.box_pattern, 0, 1, 1, 2)
        self.gridLayout_2.setColumnMinimumWidth(0, 70)
        self.tab_tracks.addTab(self.tab_parse, "")
        self.tab_info = QtWidgets.QWidget()
        self.tab_info.setObjectName("tab_info")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_info)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.visual_gram = QAudioChartView(self.tab_info)
        self.visual_gram.setMinimumSize(QtCore.QSize(0, 150))
        self.visual_gram.setObjectName("visual_gram")
        self.gridLayout_3.addWidget(self.visual_gram, 0, 0, 1, 6)
        self.edit_timestamp = QtWidgets.QLineEdit(self.tab_info)
        self.edit_timestamp.setMaximumSize(QtCore.QSize(120, 16777215))
        self.edit_timestamp.setObjectName("edit_timestamp")
        self.gridLayout_3.addWidget(self.edit_timestamp, 1, 4, 1, 1)
        self.btn_pause_play = QtWidgets.QPushButton(self.tab_info)
        self.btn_pause_play.setMaximumSize(QtCore.QSize(40, 40))
        self.btn_pause_play.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/player/play"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/player/pause"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_pause_play.setIcon(icon)
        self.btn_pause_play.setIconSize(QtCore.QSize(25, 25))
        self.btn_pause_play.setCheckable(True)
        self.btn_pause_play.setFlat(True)
        self.btn_pause_play.setObjectName("btn_pause_play")
        self.gridLayout_3.addWidget(self.btn_pause_play, 1, 0, 1, 1)
        self.lbl_timestamp = QtWidgets.QLabel(self.tab_info)
        self.lbl_timestamp.setObjectName("lbl_timestamp")
        self.gridLayout_3.addWidget(self.lbl_timestamp, 1, 3, 1, 1)
        self.btn_paste_timestamp = QtWidgets.QPushButton(self.tab_info)
        self.btn_paste_timestamp.setObjectName("btn_paste_timestamp")
        self.gridLayout_3.addWidget(self.btn_paste_timestamp, 1, 5, 1, 1)
        self.table_tracks = QtWidgets.QTableView(self.tab_info)
        self.table_tracks.setAcceptDrops(True)
        self.table_tracks.setProperty("showDropIndicator", True)
        self.table_tracks.setDragEnabled(True)
        self.table_tracks.setDragDropOverwriteMode(False)
        self.table_tracks.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.table_tracks.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.table_tracks.setAlternatingRowColors(True)
        self.table_tracks.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.table_tracks.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_tracks.setObjectName("table_tracks")
        self.gridLayout_3.addWidget(self.table_tracks, 2, 0, 1, 6)
        self.btn_next_2 = QtWidgets.QPushButton(self.tab_info)
        self.btn_next_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_next_2.setObjectName("btn_next_2")
        self.gridLayout_3.addWidget(self.btn_next_2, 3, 5, 1, 1, QtCore.Qt.AlignRight)
        self.btn_stop = QtWidgets.QPushButton(self.tab_info)
        self.btn_stop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/player/stop"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon1)
        self.btn_stop.setIconSize(QtCore.QSize(25, 25))
        self.btn_stop.setFlat(True)
        self.btn_stop.setObjectName("btn_stop")
        self.gridLayout_3.addWidget(self.btn_stop, 1, 1, 1, 1)
        self.btn_prev_1 = QtWidgets.QPushButton(self.tab_info)
        self.btn_prev_1.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_prev_1.setObjectName("btn_prev_1")
        self.gridLayout_3.addWidget(self.btn_prev_1, 3, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 2, 1, 1)
        self.tab_tracks.addTab(self.tab_info, "")
        self.tab_sheets = QtWidgets.QWidget()
        self.tab_sheets.setObjectName("tab_sheets")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_sheets)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_save = QtWidgets.QPushButton(self.tab_sheets)
        self.btn_save.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_4.addWidget(self.btn_save, 2, 2, 1, 1)
        self.edit_cue_sheets = QtWidgets.QTextEdit(self.tab_sheets)
        self.edit_cue_sheets.setObjectName("edit_cue_sheets")
        self.gridLayout_4.addWidget(self.edit_cue_sheets, 0, 0, 1, 3)
        self.btn_prev_2 = QtWidgets.QPushButton(self.tab_sheets)
        self.btn_prev_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_prev_2.setObjectName("btn_prev_2")
        self.gridLayout_4.addWidget(self.btn_prev_2, 2, 0, 1, 1)
        self.tab_tracks.addTab(self.tab_sheets, "")
        self.gridLayout.addWidget(self.tab_tracks, 8, 0, 1, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 678, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.tab_tracks.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vexillum"))
        self.lbl_date.setText(_translate("MainWindow", "Дата", "Date"))
        self.lbl_disknumber.setText(_translate("MainWindow", "№ диска", "Disc number"))
        self.lbl_artist.setText(_translate("MainWindow", "Исполнитель", "Artist"))
        self.lbl_filename.setText(_translate("MainWindow", "Имя файла", "Filename"))
        self.lbl_comment.setText(_translate("MainWindow", "Комментарий", "Comment"))
        self.btn_filedialog.setText(_translate("MainWindow", ".."))
        self.lbl_album.setText(_translate("MainWindow", "Альбом", "Album"))
        self.lbl_pattern.setText(_translate("MainWindow", "Шаблон", "Pattern"))
        self.btn_next_1.setText(_translate("MainWindow", "Далее", "Next"))
        self.tab_tracks.setTabText(self.tab_tracks.indexOf(self.tab_parse), _translate("MainWindow", "Исходные данные", "Input data"))
        self.lbl_timestamp.setText(_translate("MainWindow", "Временная отметка:", "Timestamp"))
        self.btn_paste_timestamp.setText(_translate("MainWindow", "Вставить", "Paste"))
        self.btn_next_2.setText(_translate("MainWindow", "Далее", "Next"))
        self.btn_prev_1.setText(_translate("MainWindow", "Назад", "Next"))
        self.tab_tracks.setTabText(self.tab_tracks.indexOf(self.tab_info), _translate("MainWindow", "Композиции", "Tracks"))
        self.btn_save.setText(_translate("MainWindow", "Сохранить", "Save"))
        self.btn_prev_2.setText(_translate("MainWindow", "Назад", "Next"))
        self.tab_tracks.setTabText(self.tab_tracks.indexOf(self.tab_sheets), _translate("MainWindow", "Cue результат", "Cue sheet"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

from audio_helper import QAudioChartView
import player_icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

