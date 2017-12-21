# -*- coding: utf-8 -*-
import sys
import MeCab

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class FileNameDialog(QWidget):
    title = '形態素解析するファイルを選択'
    left, top, width, height = 10, 10, 640, 480

    def open(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileNames(
            self, self.title, "", "Text File (*.txt)", options=options)
        return fileName

def show_words(text):
    # 辞書にneologdを使用
    m = MeCab.Tagger("/usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    list_parse_text = m.parse(text).split("\n")
    for p_text in list_parse_text:
        if p_text.find("名詞,一般") >= 0 or p_text.find("名詞,固有名詞") >= 0:
            print(p_text[:-1].split("\t")[0] + " ", end="")

def main():
    app = QApplication(sys.argv)
    # sys.exit(app.exec_())
    dialog = FileNameDialog()
    fileName = dialog.open()
    dialog.close()
    if fileName:
        for tmp_fname in fileName:
            with open(tmp_fname, 'r') as f:
                text = f.read()
                show_words(text)
            # ファイルが2つ以上ならば改行する．それ以外はしない．
            if len(fileName) >= 2:
                print("\n")

if __name__ == '__main__':
    main()
