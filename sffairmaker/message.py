#encoding:shift-jis
from __future__ import division, print_function, unicode_literals
from sffairmaker.qutil import *
from sffairmaker import (
    const,
    version
)
import os.path

class Message:
    def warningMsg(self, text, parent):
        box = QMessageBox(parent)
        box.setIcon(QMessageBox.Warning)
        box.setTextFormat(Qt.PlainText)
        box.setWindowTitle(const.Title)
        box.setText(text)
        return box.exec_()
    
    def confirmMsg(self, text, parent):
        box = QMessageBox(parent)
        box.setIcon(QMessageBox.Warning)
        box.setTextFormat(Qt.PlainText)
        box.setWindowTitle(const.Title)
        box.setText(text)
        
        box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return box.exec_() == QMessageBox.Ok
        
    def invaildImageFormatMsg(self, filename, parent=None):
        if os.path.isfile(filename):
            text = u'"{0}"��ǂݍ��߂܂���B�Ή����Ă��Ȃ��摜�`���ł��B'.format(filename)
        else:
            text = u'"{0}"��������܂���B'.format(filename)
        return self.warningMsg(text, parent)
    
    def invaildFormatMsg(self, filename, parent=None):
        if os.path.isfile(filename):
            text = u'"{0}"��ǂݍ��߂܂���B���Ă��邩�A�Ή����Ă��Ȃ��`���ł��B'.format(filename)
        else:
            text = u'"{0}"��������܂���B'.format(filename)
        return self.warningMsg(text, parent)
    
    def invalidSprIndexMsg(self, parent=None):
        text = u"�������摜�ԍ����w�肵�Ă��������B"
        return self.warningMsg(text, parent)
    
    def saveImageErrorMsg(self, filename, parent=None):
        text = u'�摜��"{0}"�ɕۑ��ł��܂���ł����B'.format(filename)
        return self.warningMsg(text, parent)
    
    def saveErrorMsg(self, filename, parent=None):
        text = u'"{0}"�ɕۑ��ł��܂���ł����B'.format(filename)
        return self.warningMsg(text, parent)
    
    def createDirErrorMsg(self, dirname, parent=None):
        text = u'�V�����t�H���_"{0}"����邱�Ƃ��o���܂���ł����B'.format(filename)
        return self.warningMsg(text, parent)
    
    def actionParsingErrorMsg(self, lineno, line, parent=None):
        text = u"�s '{0}' ���p�[�X�ł��܂���ł����B".format(line)
        return self.warningMsg(text, parent)
    
    def actionParsingSectionNameErrorMsg(self, section_name, parent=None):
        text = u"�Z�N�V������ '{0}' ���p�[�X�ł��܂���ł����B".format(section_name)
        return self.warningMsg(text, parent)

    def noUnusedColorMsg(self, parent=None):
        text = u"���g�p�F�������A�w�i�F���m�ۂł��܂���ł����B"
        return self.warningMsg(text, parent)

    def cannotOpenFileMsg(self, filename, parent=None):
        if os.path.isfile(filename):
            text = u'"{0}"���J���܂���B'.format(filename)
        else:
            text = u'"{0}"��������܂���B'.format(filename)
        return self.warningMsg(text, parent)
    
    def cannotSaveFileMsg(self, filename, parent=None):
        text = u'"{0}"�ɕۑ��ł��܂���ł����B���̃v���O��������g�p����Ă���\��������܂��B'.format(filename)
        return self.warningMsg(text, parent)
    
    def askReloadModified(self, name, parent=None):
        text = (u'{0}�͕ύX����Ă��܂��B\n'
                u'�ēǂݍ��݂���ƕύX�������e�������܂����A��낵���ł����H').format(name)
        return self.confirmMsg(text, parent)
    
    def aboutQtVersion(self):
        QMessageBox.aboutQt(None)
        
    def aboutVersion(self):
        text = u"<h1>SFFAIRMaker2</h1>"
        from string import Template
        
        t = Template(VersionInfoText)
        infoText = t.substitute(**vars(version))
        
        msgBox = QMessageBox()
        msgBox.setWindowTitle("About SFFAIRMaker")
        msgBox.setText(text)
        msgBox.setInformativeText(infoText)
        msgBox.exec_()

    def cannotPopenMsg(self, cmd, parent=None):
        text = (u"�O���v���Z�X���N���ł��܂���ł����B\n"
                u"�R�}���h='{0}'".format(cmd))
        return self.warningMsg(text, parent)

VersionInfoText = u"""
<html>
<head>
<style>
table {
  border-style:none;
}
td {
  border-style:none;
}
tr {
  border-style:none;
}

td.key:after {
}
td.val:before {
  content:": ";
}

</style>
</head>

<body>
<table>
  <tr><td class="key">name   <td class="val">$name
  <tr><td class="key">version<td class="val">$version
  <tr><td class="key">author <td class="val">$author
  <tr><td class="key">url    <td class="val"><a href='$url'>$url</a>
  <tr><td class="key">lisence<td class="val">$license_name
</table>
<address>
$copyright
</address>
</body>
</html>
"""
    
def main():
    app = QApplication([])
##    invaildImageFormat("D:\\owner\\My Documents\\Python\\sffairmaker\\sffairmaker\\kfm.sff", None)
    
    Message().aboutVersion()
    
    
    
if "__main__" == __name__:
    main()