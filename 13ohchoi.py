# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '10ohchoi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# 주간근무량, 식당안내, 여맺마 근무량 삽입. revised on 2020.2.20.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import numpy as np
import glob, os
from matplotlib import pyplot as plt, rcParams, font_manager
import math
from PyQt5.QtGui import QPixmap
import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_upload = QtWidgets.QPushButton(self.centralwidget)
        self.btn_upload.setGeometry(QtCore.QRect(660, 135, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.btn_upload.setFont(font)
        self.btn_upload.setObjectName("btn_upload")
        self.start_mon = QtWidgets.QComboBox(self.centralwidget)
        self.start_mon.setGeometry(QtCore.QRect(84, 43, 104, 26))
        self.start_mon.setEditable(True)
        self.start_mon.setDuplicatesEnabled(True)
        self.start_mon.setObjectName("start_mon")
        self.start_week = QtWidgets.QComboBox(self.centralwidget)
        self.start_week.setGeometry(QtCore.QRect(188, 43, 104, 26))
        self.start_week.setEditable(True)
        self.start_week.setDuplicatesEnabled(True)
        self.start_week.setObjectName("start_week")
        self.end_mon = QtWidgets.QComboBox(self.centralwidget)
        self.end_mon.setGeometry(QtCore.QRect(370, 43, 104, 26))
        self.end_mon.setEditable(True)
        self.end_mon.setDuplicatesEnabled(True)
        self.end_mon.setObjectName("end_mon")
        self.end_week = QtWidgets.QComboBox(self.centralwidget)
        self.end_week.setGeometry(QtCore.QRect(474, 43, 104, 26))
        self.end_week.setEditable(True)
        self.end_week.setDuplicatesEnabled(True)
        self.end_week.setObjectName("end_week")
        self.lbl_start = QtWidgets.QLabel(self.centralwidget)
        self.lbl_start.setGeometry(QtCore.QRect(150, 20, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.lbl_start.setFont(font)
        self.lbl_start.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_start.setObjectName("lbl_start")
        self.lbl_end = QtWidgets.QLabel(self.centralwidget)
        self.lbl_end.setGeometry(QtCore.QRect(430, 20, 90, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.lbl_end.setFont(font)
        self.lbl_end.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_end.setObjectName("lbl_end")
        self.btn_disp_image = QtWidgets.QPushButton(self.centralwidget)
        self.btn_disp_image.setGeometry(QtCore.QRect(660, 255, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.btn_disp_image.setFont(font)
        self.btn_disp_image.setObjectName("btn_disp_image")
        self.tableview = QtWidgets.QTableView(self.centralwidget)
        self.tableview.setGeometry(QtCore.QRect(10, 75, 643, 480))
        self.tableview.setObjectName("tableview")
        self.btn_save_image = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save_image.setGeometry(QtCore.QRect(660, 195, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.btn_save_image.setFont(font)
        self.btn_save_image.setObjectName("btn_save_image")
        self.btn_path = QtWidgets.QPushButton(self.centralwidget)
        self.btn_path.setGeometry(QtCore.QRect(660, 75, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.btn_path.setFont(font)
        self.btn_path.setObjectName("btn_path")
        self.btn_open_image = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_image.setGeometry(QtCore.QRect(660, 505, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.btn_open_image.setFont(font)
        self.btn_open_image.setObjectName("btn_open_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 여기부터 jsha python code
        self.statusbar.setStyleSheet("background-color: white; color: black")
        self.tableview.columnSpan(10, 20)
        self.tableview.setShowGrid(True)
        self.tableview.show()

        # 한글설정
        rcParams['font.sans-serif'] = 'Source Han Sans K'
        rcParams['font.weight'] = 'regular'
        rcParams['axes.titlesize'] = 15
        rcParams['ytick.labelsize'] = 12
        rcParams['xtick.labelsize'] = 12

        mon_items = [str(i) + '월' for i in range(1, 13)]
        week_items = [str(i) + '주' for i in range(1, 7)]
        self.start_mon.addItems(mon_items)
        self.start_week.addItems(week_items)
        self.end_mon.addItems(mon_items)
        self.end_week.addItems(week_items)

        self.btn_upload.clicked.connect(self.go_upload)
        self.btn_save_image.clicked.connect(self.save_image)
        self.btn_disp_image.clicked.connect(self.disp_image)
        self.btn_path.clicked.connect(self.find_path)
        self.btn_open_image.clicked.connect(self.open_image)
        self.texting = 'welcome to this program \n'
        self.statusbar.showMessage(self.texting)

        self.display_window = QtWidgets.QFrame()
        self.disp_ui = Ui_display_frame()
        self.disp_ui.setupUi(self.display_window)

        self.s01 = '-'
        self.s02 = '-'
        self.e01 = '-'
        self.e02 = '-'

        #self.base_dir = '/Users/jsha/PycharmProjects/ohchoi/2020'
        self.base_dir = os.getcwd()
        self.filepath = self.base_dir
        self.image_dir = os.path.join(self.filepath, 'images')

        self.analyzing = False

        global imagelist
        imagelist = []

    def go_upload(self):
        self.s01 = self.start_mon.currentText()
        self.s02 = self.start_week.currentText()
        self.e01 = self.end_mon.currentText()
        self.e02 = self.end_week.currentText()
        self.s1 = self.s01.rstrip('월')
        self.s2 = self.s02.rstrip('주')
        self.e1 = self.e01.rstrip('월')
        self.e2 = self.e02.rstrip('주')

        self.sn = int(self.s1 + self.s2)
        self.en = int(self.e1 + self.e2)

        self.dict_files = {}
        flist_name = glob.glob('*.xlsx')
        for i in flist_name:
            m1 = re.findall('\d+', i)
            m2 = int(m1[0]+m1[1])
            self.dict_files[m2] = i

        flist_total_num = list(self.dict_files.keys())
        self.flist_num = [i for i in flist_total_num if i >= self.sn and i <= self.en]
        #self.flist = [dict_files[i] for i in flist_num]
        #print(self.flist_num)

        if self.sn > self.en:
            self.texting = '시작 주와 마지막 주를 다시 확인하세요. 시작 주는 마지막 주보다 빨라야 합니다. \n'
            self.statusbar.showMessage(self.texting)
            self.analyzing = False
        elif not self.flist_num:
            self.analyzing = False
            self.no_analyzing()
        else:
            self.texting = '{} {}부터 {} {}까지 총 {}개의 파일을 분석합니다. \n'.format(self.s01, self.s02, self.e01, self.e02,
                                                                          len(self.flist_num))
            self.statusbar.showMessage(self.texting)
            self.analyzing = True
            self.do_analyzing()


    def no_analyzing(self):
        self.texting = '{} {}부터 {} {}까지 분석할 파일이 없습니다. PATH를 확인하고, 시작주, 마지막주, Upload를 다시 수행하세요.\n'.format(self.s01,
                                                                                                         self.s02,                                                                                                  self.e01,
                                                                                                         self.e02)
        self.statusbar.showMessage(self.texting)
        df = pd.DataFrame([])  # 빈 df를 넘겨서 테이블을 없앨려고 하는 것임. 계속 이 모델 방식을 써야할 듯.
        model = MyTableModel(df)
        self.tableview.setModel(model)
        self.tableview.show()

    def do_analyzing(self):
        self.rawappdata = pd.DataFrame([])
        col_list = []
        self.namelist = []
        self.nightlist = []
        self.jangbilist = []
        self.safelist = []
        self.dininglist =[]
        for file_num in self.flist_num:
            file_num = str(file_num)
            y = file_num[:-1]
            w = file_num[-1]
            mw = y + w

            col_name = ['name' + mw, 'total' + mw, 'night' + mw, 'jangbi' + mw, 'safe' + mw, 'dining' + mw]
            col_list += col_name
            data = pd.read_excel(self.dict_files[int(file_num)], encoding='cp949',
                               names=col_name,
                               skiprows=84, usecols=[17, 28, 31, 34, 37, 40])

            #data = data[:35].dropna()  # 35은 현동쌤까지.
            data = data[:40].dropna(how='all')  # 모든 행 값이 NaN 일때 그 해당 행을 삭제.
            self.rawappdata = pd.concat([self.rawappdata, data], axis=1, sort=False)

        self.rawappdata = self.rawappdata.replace([0.0, 0, '0'], np.nan) # NaN으로 만들어서 쉽게 제거할려고 설정
        self.rawappdata = self.rawappdata.dropna(how='all') #이름이 아예 없는 빈 행 제거

        self.namelist = [col_list[i] for i in range(len(col_list)) if i % 6 == 0]
        #        namelist = list(set(namelist))  # 중복제거
        self.totallist = [col_list[i] for i in range(len(col_list)) if i % 6 == 1]
        self.nightlist = [col_list[i] for i in range(len(col_list)) if i % 6 == 2]
        self.jangbilist = [col_list[i] for i in range(len(col_list)) if i % 6 == 3]
        self.safelist = [col_list[i] for i in range(len(col_list)) if i % 6 == 4]
        self.dininglist = [col_list[i] for i in range(len(col_list)) if i % 6 == 5]

        self.appdata2 = self.rawappdata[self.namelist] #왠지 모르지만, 아예 새로운 DataFrame을 만들어야 해서.
        self.appdata2.dropna(axis=1, inplace=True) # 이름 중에 NaN이 하나라도 있으면 그 열 제거
        self.appdata2.drop(self.appdata2.columns[1:], axis=1, inplace=True) # 여러개 중에 하나만 남기고 제거
        self.newnamelist = [self.appdata2.columns[0]] # 하나의 이름 열만 이제 새로 사용
        print('newnamelist', self.newnamelist)

        self.appdata = self.rawappdata.drop(self.namelist, axis=1)
        self.appdata = pd.concat([self.appdata2, self.appdata], axis=1, sort=False)
        self.appdata[self.totallist] = self.appdata[self.totallist].replace(np.nan, 0.)
        self.appdata[self.nightlist] = self.appdata[self.nightlist].replace(np.nan, 0.)
        #self.appdata[self.nightlist] = self.appdata[self.nightlist].astype(np.float)
        self.appdata[self.jangbilist] = self.appdata[self.jangbilist].replace(np.nan, 0.)
        self.appdata[self.safelist] = self.appdata[self.safelist].replace(np.nan, 0.)
        self.appdata[self.dininglist] = self.appdata[self.dininglist].replace(np.nan, 0.)

        # appdata.dropna(inplace=True) # data 중 하나라도 Nan이면, 이 행은 그냥 drop!!
        self.appdata = self.appdata.dropna()  # 위 function과 동일
        # self.win_display.append(appdata[named])
        #        print(appdata[totallist].sum(axis=1))
        #        print(appdata[namelist])  # 자료가 누락되지 않고 column별로 잘 들어왔나 확인
        #        print(appdata[nightlist])  # 이름 중복 제거

        #        totalsum = appdata[total].sum(axis=1)  # Series 형식
        #        nightsum = appdata[night].sum(axis=1)
        #        jangbisum = appdata[jangbi].sum(axis=1)
        #        minval = [totalsum[:].min(), nightsum[:].min(), jangbisum[:].min()]
        #        maxval = [totalsum[:].max(), nightsum[:].max(), jangbisum[:].max()]
        #        plotlist = [totalsum, nightsum, jangbisum]
        self.appdata["totalsum"] = self.appdata[self.totallist].sum(axis=1)  # "totalsum"이라는 새로운 컬럼을 appdata에 추가
        self.appdata["nightsum"] = self.appdata[self.nightlist].sum(axis=1)  # "nightsum"이라는 새로운 컬럼을 appdata에 추가
        self.appdata["jangbisum"] = self.appdata[self.jangbilist].sum(axis=1)
        self.appdata["safesum"] = self.appdata[self.safelist].sum(axis=1)
        self.appdata["diningsum"] = self.appdata[self.dininglist].sum(axis=1)
        self.appdata['onlyday'] = self.appdata.apply(lambda x: self.subtract(x['totalsum'], x['nightsum']), axis=1)

        self.sumlist = ["totalsum", "nightsum", 'onlyday', "jangbisum", 'safesum', 'diningsum']  # 새로이 추가된 컬럼 이름을 리스트로 묶음
        #print(self.appdata.loc[self.appdata["name11"]=='상록', ['dining11', 'dining12', 'diningsum']])
        #        print('행 수 = ', self.appdata.shape[0])
        #        print('열 수 = ', self.appdata.shape[1])

        #        model = MyTableModel(self.appdata)  # appdata 전부다 넘김
        #        model = MyTableModel(self.appdata[self.namelist + self.sumlist])    # appdata의 name columns & sum columns
        model = MyTableModel(self.rawappdata)  # appdata의 name columns만 넘김
        self.tableview.setModel(model)
        self.tableview.show()

    def subtract(self, total, night):
        return total - night

    def save_image(self):
        if self.analyzing is False:
            self.no_saving_image()
        else:
            self.do_saving_image()

    def no_saving_image(self):
        global imagelist
        imagelist = []
        self.texting = '{} {}부터 {} {}까지 분석할 데이터, 저장할 이미지가 없습니다. Data Update를 해 주세요.\n'.format(self.s01, self.s02, self.e01, self.e02)
        self.statusbar.showMessage(self.texting)

    def do_saving_image(self):
        print('plot graph')
        # self.appdata dataframe에서 컬럼이름으로 데이터를 쉽게 가져오기 위해 컬럼 이름들을 아래와 같이 리스트화 함.
        # 컬럼 이름 리스트:  self.namelist, self.totallist, self.nightlist, self.jangbilist, self.sumlist
        # self.sumlist = ["totalsum", "nightsum", "jangbisum"]
        # 데이터 access 방법: self.appdata[namelist], self.appdata[totallist], self.appdata[namelist + nightlist]
        # 리스트를 이용하지 않고 컬럼 이름으로 바로 access 하는 방법: self.appdata[namelist0], self.appdata["totalsum"]
        # print(self.appdata[self.namelist + self.sumlist])

        minval = [self.appdata["totalsum"].min(), self.appdata["nightsum"].min(), self.appdata['onlyday'].min(),
                  self.appdata["jangbisum"].min(), self.appdata["safesum"].min(), self.appdata["diningsum"].min()]
        maxval = [self.appdata["totalsum"].max(), self.appdata["nightsum"].max(), self.appdata['onlyday'].max(),
                  self.appdata["jangbisum"].max(), self.appdata["safesum"].max(), self.appdata["diningsum"].max()]
        plotlist = [self.appdata[i] for i in self.sumlist]
        # plotlist = [self.appdata["totalsum"], self.appdata["nightsum"], self.appdata["jangbisum"]

        xlab = '이름'
        ylab = '근무량'
        titlelist = ['총 근무량', '야간 근무량', '주간 근무량', '장비 근무량', '안전교육 근무량', '식사-방송 근무량']

        if os.path.exists('images') is False:
            os.mkdir('images')
        self.image_dir = os.path.join(self.filepath, 'images')

        global imagelist
        imagelist = []

        for i in range(len(titlelist)):
            fig = plt.figure(figsize=(14, 7))
            ax = fig.add_subplot(111)
            ax.grid(axis='y')
            ax.bar(self.appdata[self.namelist[0]], plotlist[i],
                   label='{} max: {}'.format(titlelist[i], maxval[i]))
            imagename = self.s1 + '월' + self.s2 + '주' + '_' + self.e1 + '월' + self.e2 + '주' + '_' + titlelist[i]
            print(imagename)

            ax.set_title(imagename, size=15)
            ax.set_ylabel(ylab, size=15)

            imagename = imagename + '.png'

            ax.tick_params(axis='both', which='major', labelsize=12)

            diff_maxmin = math.ceil(maxval[i]) - math.floor(minval[i])
            if diff_maxmin <= 20:
                step_yticks = math.ceil(diff_maxmin / 20)
                print(step_yticks)
            elif diff_maxmin > 10 and diff_maxmin <= 50:
                step_yticks = math.ceil(diff_maxmin / 25)
                print(step_yticks)
            else:
                step_yticks = 5
                print(step_yticks)

            if minval[i] != 0. and maxval[i] != 0:
                ax.set_yticks(range(math.floor(minval[i]), math.ceil(maxval[i]), step_yticks))
            # np.round(int(maxval[i],-1),
            ax.legend()

            plt.savefig(os.path.join(self.image_dir, imagename))
            imagelist.append(os.path.join(self.image_dir, imagename))

            self.texting = "근무량 통계 그래프를 {} 디렉토리에 이미지 파일로 저장하였습니다.".format(self.image_dir)
            self.statusbar.showMessage(self.texting)

        # plt.show()

        #        self.start_mon.clearEditText()
        #        self.start_week.clearEditText()
        #        self.end_mon.clearEditText()
        #        self.end_week.clearEditText()

    def disp_image(self):
        global imagelist
        if not imagelist:
            self.no_disp_image()
        else:
            self.do_disp_image()

    def no_disp_image(self):
        self.texting = '표시할 이미지가 존재하지 않습니다.'
        self.statusbar.showMessage(self.texting)

    def do_disp_image(self):
        global imagelist, glb_num
        glb_num = 0
        print('display images')
        print(imagelist)

        self.display_window.show()

        # pixmap = QPixmap(imagelist[glb_num]).scaled(1000, 500)
        pixmap = QPixmap(imagelist[glb_num])
        self.disp_ui.lbl_image.setPixmap(pixmap)
        self.disp_ui.lbl_image.resize(pixmap.width(), pixmap.height())

        self.texting = '{} 외 {} 개의 이미지를 표시합니다.'.format(imagelist[0], len(imagelist))
        self.statusbar.showMessage(self.texting)

    def find_path(self):
        # filepath, _ = QFileDialog.getOpenFileName(MainWindow, "working_dir", os.getcwd(), "csv (*.csv)")
        self.filepath = QFileDialog.getExistingDirectory(MainWindow, caption='Select directory',
                                                         directory=self.base_dir, options=QFileDialog.ShowDirsOnly)
        if self.filepath:
            os.chdir(self.filepath)
            self.texting = '파일 경로를 {}로 변경합니다.'.format(self.filepath)
            self.statusbar.showMessage(self.texting)
        else:
            os.chdir(self.base_dir)
            self.texting = 'PATH를 눌러 파일 경로를 새로 지정해 주세요. 아니면 {}가 default 경로로 설정됩니다.'.format(self.base_dir)
            self.statusbar.showMessage(self.texting)

    def open_image(self):
        global imagelist
        if not os.path.exists(self.image_dir):
            self.texting = 'image 저장 디렉토리가 존재하지 않습니다. Upload와 Save Image를 먼저 수행하세요.'
            self.statusbar.showMessage(self.texting)
        else:
            imagetuple = QFileDialog.getOpenFileNames(MainWindow, caption='Choose the images',
                                                         directory=self.image_dir)
            if imagetuple[0]:
                imagelist = list(imagetuple)[:][0]
                self.texting = '{} 외 {} 개의 이미지를 불러옵니다.'.format(imagelist[0], len(imagelist))
                self.statusbar.showMessage(self.texting)
            else:
                self.texting = '불러온 이미지가 없습니다.'
                self.statusbar.showMessage(self.texting)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analyzing the amount of Work"))
        self.btn_upload.setText(_translate("MainWindow", "Upload Data"))
        self.lbl_start.setText(_translate("MainWindow", "Start Week"))
        self.lbl_end.setText(_translate("MainWindow", "End Week"))
        self.btn_disp_image.setText(_translate("MainWindow", "Display"))
        self.btn_save_image.setText(_translate("MainWindow", "Save Image"))
        self.btn_path.setText(_translate("MainWindow", "Set PATH"))
        self.btn_open_image.setText(_translate("MainWindow", "Open Image"))

class Ui_display_frame(object):
    def setupUi(self, display_frame):
        display_frame.setObjectName("display_frame")
        display_frame.resize(1440, 800)
        display_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        display_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_image = QtWidgets.QLabel(display_frame)
        self.lbl_image.setGeometry(QtCore.QRect(10, 10, 1420, 730))
        self.lbl_image.setText("")
        self.lbl_image.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_image.setObjectName("lbl_image")
        self.btn_pre = QtWidgets.QPushButton(display_frame)
        self.btn_pre.setGeometry(QtCore.QRect(500, 740, 210, 50))
        self.btn_pre.setObjectName("btn_pre")
        self.btn_post = QtWidgets.QPushButton(display_frame)
        self.btn_post.setGeometry(QtCore.QRect(730, 740, 210, 50))
        self.btn_post.setObjectName("btn_post")

        self.retranslateUi(display_frame)
        QtCore.QMetaObject.connectSlotsByName(display_frame)

        self.btn_pre.clicked.connect(self.disp_pre)
        self.btn_post.clicked.connect(self.disp_post)

    def disp_pre(self):
        global imagelist, glb_num
        glb_num -= 1

        if glb_num < 0:
            print("There is no image. Please check")
            pixmap = QPixmap(None)
            self.lbl_image.setPixmap(pixmap)
            glb_num += 1
        else:
            #pixmap = QPixmap(imagelist[glb_num]).scaled(1000, 500)
            pixmap = QPixmap(imagelist[glb_num])
            self.lbl_image.setPixmap(pixmap)
            self.lbl_image.resize(pixmap.width(), pixmap.height())

    def disp_post(self):
        global imagelist, glb_num
        glb_num += 1

        if glb_num >= len(imagelist):
            print("There is no image. Please check")
            pixmap = QPixmap(None)
            self.lbl_image.setPixmap(pixmap)
            glb_num -= 1
        else:
            #pixmap = QPixmap(imagelist[glb_num]).scaled(1000, 500)
            pixmap = QPixmap(imagelist[glb_num])
            self.lbl_image.setPixmap(pixmap)
            self.lbl_image.resize(pixmap.width(), pixmap.height())

    def retranslateUi(self, display_frame):
        _translate = QtCore.QCoreApplication.translate
        display_frame.setWindowTitle(_translate("display_frame", "Display Image"))
        self.btn_pre.setText(_translate("display_frame", "Previous"))
        self.btn_post.setText(_translate("display_frame", "Post"))


class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
#            return self.header[col]
        return None

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

