# Form implementation generated from reading ui file 'YTDWindowUI.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


#! My codes

from cgitb import enable
from re import S
from tkinter.filedialog import Open
from urllib import response
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog,QMessageBox
from PyQt6.QtGui import QPixmap
import sys,subprocess
# My YTD APP module file
import ytd
from pathlib import Path
import os
from os.path import splitext
import requests
import shutil

#* If download_path.txt exists set default download folder to that
try: 
    with open('cache\download_path.txt','r') as file:
        for line in file:
            download_folder_default_path = line
                    
except:
    download_folder_default_path = str(os.path.join(Path.home(), 'Downloads'))




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1000, 700)
        Form.setMinimumSize(QtCore.QSize(1000, 700))
        Form.setMaximumSize(QtCore.QSize(1000, 700))
        font = QtGui.QFont()
        font.setPointSize(6)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/YTD-Logo-Purple.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(24, 24, 24);")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(-40, 120, 1081, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 15, 100, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/YTD-Logo-Purple.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.DonateBtn = QtWidgets.QPushButton(Form)
        self.DonateBtn.setGeometry(QtCore.QRect(460, 30, 230, 70))
        font = QtGui.QFont()
        font.setFamily("Trekker")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.DonateBtn.setFont(font)
        self.DonateBtn.setStyleSheet("background-color: rgba(80, 71, 128, 100);\n"
"color:white;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/bitcoin.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.DonateBtn.setIcon(icon1)
        self.DonateBtn.setIconSize(QtCore.QSize(30, 30))
        self.DonateBtn.setObjectName("DonateBtn")
        self.ReportBtn = QtWidgets.QPushButton(Form)
        self.ReportBtn.setGeometry(QtCore.QRect(740, 30, 231, 70))
        font = QtGui.QFont()
        font.setFamily("Trekker")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.ReportBtn.setFont(font)
        self.ReportBtn.setStyleSheet("background-color: rgba(80, 71, 128, 100);\n"
"color:white;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("image/bug.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ReportBtn.setIcon(icon2)
        self.ReportBtn.setIconSize(QtCore.QSize(30, 30))
        self.ReportBtn.setObjectName("ReportBtn")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 35, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Trekker")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        self.LinkLabel = QtWidgets.QLabel(Form)
        self.LinkLabel.setGeometry(QtCore.QRect(70, 150, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Trekker")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.LinkLabel.setFont(font)
        self.LinkLabel.setStyleSheet("color:white")
        self.LinkLabel.setObjectName("LinkLabel")
        self.VideoLink = QtWidgets.QLineEdit(Form)
        self.VideoLink.setGeometry(QtCore.QRect(70, 190, 691, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.VideoLink.setFont(font)
        self.VideoLink.setStyleSheet("background-color:white;")
        self.VideoLink.setClearButtonEnabled(False)
        self.VideoLink.setObjectName("VideoLink")
        self.FindBtn = QtWidgets.QPushButton(Form)
        self.FindBtn.setEnabled(False)
        self.FindBtn.setGeometry(QtCore.QRect(780, 190, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Trekker")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.FindBtn.setFont(font)
        self.FindBtn.setStyleSheet("background-color: rgba(74, 249, 255, 100);\n"
"color: rgb(0, 0, 0);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("image/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.FindBtn.setIcon(icon3)
        self.FindBtn.setIconSize(QtCore.QSize(30, 30))
        self.FindBtn.setObjectName("FindBtn")
        self.VideoThumbnail = QtWidgets.QLabel(Form)
        self.VideoThumbnail.setGeometry(QtCore.QRect(70, 310, 320, 240))
        self.VideoThumbnail.setText("")
        self.VideoThumbnail.setObjectName("VideoThumbnail")
        self.LinkLabel_2 = QtWidgets.QLabel(Form)
        self.LinkLabel_2.setEnabled(True)
        self.LinkLabel_2.setGeometry(QtCore.QRect(410, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Trekker")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.LinkLabel_2.setFont(font)
        self.LinkLabel_2.setStyleSheet("color:white")
        self.LinkLabel_2.setObjectName("LinkLabel_2")
        self.VideoTitleText = QtWidgets.QPlainTextEdit(Form)
        self.VideoTitleText.setGeometry(QtCore.QRect(410, 340, 581, 201))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.VideoTitleText.setFont(font)
        self.VideoTitleText.setReadOnly(True)
        self.VideoTitleText.setObjectName("VideoTitleText")
        self.VideoTitleText.setStyleSheet('color:white;')
        self.FormatSelector = QtWidgets.QComboBox(Form)
        self.FormatSelector.setEnabled(False)
        self.FormatSelector.setGeometry(QtCore.QRect(70, 240, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.FormatSelector.setFont(font)
        self.FormatSelector.setStyleSheet("background-color:white;")
        self.FormatSelector.setIconSize(QtCore.QSize(30, 30))
        self.FormatSelector.setFrame(False)
        self.FormatSelector.setObjectName("FormatSelector")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("image/mp4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.FormatSelector.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/music-store-app.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.FormatSelector.addItem(icon5, "")
        self.VideoQualitySelector = QtWidgets.QComboBox(Form)
        self.VideoQualitySelector.setEnabled(False)
        self.VideoQualitySelector.setGeometry(QtCore.QRect(300, 240, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.VideoQualitySelector.setFont(font)
        self.VideoQualitySelector.setStyleSheet("background-color:white;")
        self.VideoQualitySelector.setIconSize(QtCore.QSize(30, 30))
        self.VideoQualitySelector.setFrame(False)
        self.VideoQualitySelector.setObjectName("VideoQualitySelector")
        self.VideoQualitySelector.addItem("")
        self.VideoQualitySelector.addItem("")
        self.VideoQualitySelector.addItem("")
        self.VideoQualitySelector.addItem("")
        self.VideoQualitySelector.addItem("")
        self.VideoQualitySelector.addItem("")
        self.VideoQualitySelector.addItem("")

        #self.AudioQualitySelector = QtWidgets.QComboBox(Form)
        #self.AudioQualitySelector.setEnabled(False)
        #self.AudioQualitySelector.setGeometry(QtCore.QRect(530, 240, 181, 51))
        #font = QtGui.QFont()
        #font.setPointSize(16)
        #self.AudioQualitySelector.setFont(font)
        #self.AudioQualitySelector.setStyleSheet("background-color:white;")
        #self.AudioQualitySelector.setIconSize(QtCore.QSize(30, 30))
        #self.AudioQualitySelector.setObjectName("AudioQualitySelector")
        #self.AudioQualitySelector.addItem("")
        #self.AudioQualitySelector.addItem("")
        
        self.DownloadPath = QtWidgets.QLineEdit(Form)
        self.DownloadPath.setGeometry(QtCore.QRect(210, 555, 610, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DownloadPath.setFont(font)
        self.DownloadPath.setStyleSheet("background-color:white;")
        self.DownloadPath.setClearButtonEnabled(False)
        self.DownloadPath.setObjectName("DownloadPath")
        self.DownloadPath.setText(download_folder_default_path)
        self.LinkLabel_3 = QtWidgets.QLabel(Form)
        self.LinkLabel_3.setEnabled(True)
        self.LinkLabel_3.setGeometry(QtCore.QRect(15, 560, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Trekker")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.LinkLabel_3.setFont(font)
        self.LinkLabel_3.setStyleSheet("color:white")
        self.LinkLabel_3.setObjectName("LinkLabel_3")
        self.BrowseBtn = QtWidgets.QPushButton(Form)
        self.BrowseBtn.setEnabled(True)
        self.BrowseBtn.setGeometry(QtCore.QRect(830, 555, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Trekker")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.BrowseBtn.setFont(font)
        self.BrowseBtn.setStyleSheet("background-color: rgb(120, 136, 191);\n"
"color: rgb(0, 0, 0);")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("image/browse.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.BrowseBtn.setIcon(icon6)
        self.BrowseBtn.setIconSize(QtCore.QSize(30, 30))
        self.BrowseBtn.setObjectName("BrowseBtn")
        self.DownloadBtn = QtWidgets.QPushButton(Form)
        self.DownloadBtn.setEnabled(True)
        self.DownloadBtn.setGeometry(QtCore.QRect(750, 610, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Trekker")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.DownloadBtn.setFont(font)
        self.DownloadBtn.setStyleSheet("background-color: rgba(103, 178, 230, 90);\n"
"color: rgb(0, 0, 0);")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("image/direct-download.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.DownloadBtn.setIcon(icon7)
        self.DownloadBtn.setIconSize(QtCore.QSize(30, 30))
        self.DownloadBtn.setObjectName("DownloadBtn")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(280, 620, 411, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        #self.AudioQualitySelector.raise_()

        self.line.raise_()
        self.label.raise_()
        self.DonateBtn.raise_()
        self.ReportBtn.raise_()
        self.label_2.raise_()
        self.LinkLabel.raise_()
        self.VideoLink.raise_()
        self.FindBtn.raise_()
        self.VideoThumbnail.raise_()
        self.VideoTitleText.raise_()
        self.LinkLabel_2.raise_()
        self.FormatSelector.raise_()
        self.VideoQualitySelector.raise_()
        
        self.LinkLabel_3.raise_()
        self.BrowseBtn.raise_()
        self.DownloadBtn.raise_()
        self.textEdit.raise_()
        self.DownloadPath.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.VideoLink, self.FormatSelector)
        Form.setTabOrder(self.FormatSelector, self.VideoQualitySelector)
        Form.setTabOrder(self.VideoQualitySelector, self.DonateBtn)
        Form.setTabOrder(self.DonateBtn, self.VideoTitleText)
        Form.setTabOrder(self.VideoTitleText, self.ReportBtn)

        Form.setTabOrder(self.ReportBtn, self.FindBtn) #self.AudioQualitySelector  #self.AudioQualitySelector,
        Form.setTabOrder(self.FindBtn, self.DownloadPath)

        Form.setTabOrder(self.DownloadPath, self.BrowseBtn)
        Form.setTabOrder(self.BrowseBtn, self.DownloadBtn)
        Form.setTabOrder(self.DownloadBtn, self.textEdit)
        
        #! YTD-APP __init__ and signals and code 
        self.SubtitleRadioBtn = QtWidgets.QRadioButton(Form)
        self.SubtitleRadioBtn.setGeometry(QtCore.QRect(750,660,101,20))
        self.SubtitleRadioBtn.setText('Subtitle')
        subtitle_font = QtGui.QFont()
        subtitle_font.setFamily('Trekker')
        subtitle_font.setPointSize(16)
        subtitle_font.setBold(True)
        subtitle_font.setWeight(50)
        self.SubtitleRadioBtn.setFont(subtitle_font)
        self.SubtitleRadioBtn.setStyleSheet('color:rgb(143, 255, 246);')
        self.SubtitleRadioBtn.setAutoExclusive(False)

        self.VideoLink.textChanged.connect(self.video_link_changed)
        self.DownloadPath.textChanged.connect(self.download_path_changed)
        self.FormatSelector.activated.connect(self.format_selector_changed)
        self.FindBtn.clicked.connect(self.find_btn_clicked)
        self.BrowseBtn.clicked.connect(self.browse_btn_clicked)
        self.DownloadBtn.clicked.connect(self.download_btn_clicked)


    # A dialog box for when the download completes
    def show_download_completed_dialog(self):
        url = self.VideoLink.text()
        not_important , title = ytd.get_infos(url)
        dialog = QMessageBox(Form)
        dialog.setWindowTitle('Download Completed')
        dialog.setText(f"{title} Download Completed")
        dialog.setStyleSheet('color:white;')
        dialog.buttonClicked.connect(self.show_download_file_open_clicked)
        dialog.exec()

    
    def show_download_file_open_clicked(self, dialog_button):
        downloaded_path = self.DownloadPath.text()
        if sys.platform == "win32":
            os.startfile(downloaded_path)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, downloaded_path])
        

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "YTD Downloader"))
        self.DonateBtn.setText(_translate("Form", "DONATE"))
        self.ReportBtn.setText(_translate("Form", "Report Bug"))
        self.label_2.setText(_translate("Form", "Youtube Downloader"))
        self.LinkLabel.setText(_translate("Form", "Link:"))
        self.VideoLink.setPlaceholderText(_translate("Form", "Please enter your video link here...."))
        self.FindBtn.setText(_translate("Form", "FIND"))
        self.LinkLabel_2.setText(_translate("Form", "Title:"))
        self.FormatSelector.setItemText(0, _translate("Form", "MP4 (Video)"))
        self.FormatSelector.setItemText(1, _translate("Form", "MP3 (Audio)"))
        self.VideoQualitySelector.setCurrentText(_translate("Form", "480p"))
        self.VideoQualitySelector.setItemText(0, _translate("Form", "144p"))
        self.VideoQualitySelector.setItemText(1, _translate("Form", "240p"))
        self.VideoQualitySelector.setItemText(2, _translate("Form", "360p"))
        self.VideoQualitySelector.setItemText(3, _translate("Form", "480p"))
        self.VideoQualitySelector.setItemText(4, _translate("Form", "720p"))
        self.VideoQualitySelector.setItemText(5, _translate("Form", "1080p"))
        self.VideoQualitySelector.setItemText(6, _translate("Form", "Highest Resolution"))
        self.VideoQualitySelector.setCurrentIndex(3)

        #self.AudioQualitySelector.setCurrentText(_translate("Form", "128kbps"))
        #self.AudioQualitySelector.setItemText(0, _translate("Form", "128kbps"))
        #self.AudioQualitySelector.setItemText(1, _translate("Form", "320kbps"))

        self.DownloadPath.setPlaceholderText(_translate("Form", "Download Path"))
        self.LinkLabel_3.setText(_translate("Form", "Download Path:"))
        self.BrowseBtn.setText(_translate("Form", "Browse"))
        self.DownloadBtn.setText(_translate("Form", "Download"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#cbcbcb;\">This App Was made by </span><span style=\" font-size:14pt; font-weight:600; color:#cbcbcb;\">Alex-M3rcer</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#cbcbcb;\">Contact Email: </span><a href=\"mailto:alex-m3rcer@outlook.com\"><span style=\" font-size:14pt; text-decoration: underline; color:#cbcbcb;\">alex-m3rcer@outlook.com</span></a></p></body></html>"))



    #! YTD-APP function (SLOT) codes

    # when video link is entered
    def video_link_changed(self):
        text = self.VideoLink.text()
        if text:
            self.FindBtn.setEnabled(True)
            self.FormatSelector.setEnabled(True)
        else:
            self.FindBtn.setEnabled(False)
            self.FormatSelector.setEnabled(False)

    # when the Format Selector has Changed
    def format_selector_changed(self):
        selected_index = self.FormatSelector.currentIndex()
        text = self.FormatSelector.currentText()[:2]
        # MP4 selected i(0)
        if not selected_index or text == 'MP4':
            self.VideoQualitySelector.setEnabled(True)
            pass
        else:
            self.VideoQualitySelector.setEnabled(False)
        # MP3 Selected i(1)
        #if selected_index or text =='MP3':
        #    self.AudioQualitySelector.setEnabled(True)
        #else:
        #    self.AudioQualitySelector.setEnabled(False)

    # Find button clicked
    def find_btn_clicked(self):
        link = self.VideoLink.text()

        thumbnail_url,title= ytd.get_infos(link= link)
        if thumbnail_url and title:
            response = requests.get(thumbnail_url, stream=True)
            
            # download the Thumbnail image and save it toe Cache foolder and set Thumbnail to that image
            thumbnail_path = thumbnail_url
            if response.status_code == 200:
                response.raw.decode_content = True

                fileformat = splitext(thumbnail_url)[1]
                thumbnail_path = f"cache/{title}{fileformat}"
                with open(thumbnail_path,'wb') as f:
                    
                    shutil.copyfileobj(response.raw,f)

                thumbnail = QPixmap(thumbnail_path)
                self.VideoTitleText.setPlainText(title) 
                self.VideoThumbnail.setPixmap(thumbnail)
                self.VideoThumbnail.setScaledContents(True)
        else:
            # TODO: V0.9.0 Raise A Dialog Box about VIDEO Not Found
            pass
    
    # when folder is selected or download path is changed
    def download_path_changed(self):
        text = self.DownloadPath.text()
        if text:
            self.DownloadBtn.setEnabled(True)
        else:
            self.DownloadBtn.setEnabled(False)
    
    # Show browse dialog and set the download path
    def browse_btn_clicked(self):
        # Open file dialog
        download_foolder_path = QtWidgets.QFileDialog.getExistingDirectory(Form,'Select Download Path',
        download_folder_default_path)
        
        if len(download_foolder_path) > 0:
            self.DownloadPath.setText(download_foolder_path)

            # save the download path to cache
            with open('cache/download_path.txt', 'w') as file:
                file.write(download_foolder_path)

        else:
            self.DownloadPath.setText(download_folder_default_path)
            download_foolder_path = QtWidgets.QFileDialog.getExistingDirectory(Form,'Select Download Path',
        download_folder_default_path)
        # TODO: V0.9.0 Add some Error handling for file dialog

    # the download button function
    def download_btn_clicked(self):
        # get the format type
        format_type = self.FormatSelector.currentText()[:3]

        if format_type:
            if format_type == 'MP4':
                self.video_download()
            if format_type == 'MP3':
                self.audio_download()
                pass
        else:
            # TODO: V0.9.0 Error handling
            pass
    
    # Get Link & Quality & Download Path
    def get_info(self,format):
        link = self.VideoLink.text()
        download_path = self.DownloadPath.text()
        if format == 'MP4':
            quality = self.VideoQualitySelector.currentText()
            return link,quality,download_path
        elif format == 'MP3':
            quality = None
            return link,download_path
            # TODO: find out a way to get different qualities
            #
        
        
    # Video Download function
    def video_download(self):
        link, quality, download_path = self.get_info(format = 'MP4')

        try:
            status = ytd.video_download(link,quality,download_path)
            if status:
                self.show_download_completed_dialog()
            else:
                # TODO: V0.9.0 Create Error dialog for download completion
                pass
        except:
            # TODO: V0.9.0 Stream Error handling
            pass
    # Audio Download function
    def audio_download(self):
        link, download_path = self.get_info(format = 'MP3')
        try:
            status = ytd.audio_download(link,download_path)
            if status:
                self.show_download_completed_dialog()
            else:
                # TODO: V0.9.0 Create Error dialog for download completion
                pass
        except:
            # TODO: V0.9.0 Audio Stream Error handling
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    #* Cache Deletion and app run
    try:
        sys.exit(app.exec())
    finally:
        #* after app Closed Delete everything in "Cache foolder"
        path = Path('cache')
        for filename in os.listdir(path):
            if(filename == 'download_path.txt'):
                continue
            os.remove(path / filename)
    