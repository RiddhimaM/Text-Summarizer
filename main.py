import argparse
import collections
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict
from collections import Counter
from nltk.stem import PorterStemmer                     #NLTK stemmer library to find root words
from statistics import pstdev
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class MainPage(QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        self.ui = loadUi('mainpage.ui', self)
        self.pushButton_2.clicked.connect(self.retrieveText)
    
    def retrieveText(self):
        statement = self.plainTextEdit.toPlainText()
        stopWords = set(stopwords.words("english"))
        numWords = {}
        sent_score = {}
        token_sent = sent_tokenize(statement)

        for sent in token_sent:
            token_words = word_tokenize(sent)
            token_words = [word for word in token_words if word.isalnum()]

            filtered = [w for w in token_words if not w in stopWords]

            for word in filtered:
                numWords[word] = numWords.get(word,0) + 1
            sent_score[sent] = sum(numWords.values())
            filtered.clear

        avg = sum(sent_score.values())/ len(sent_score)
        summary = ''
        for sentence in token_sent:
            if sentence in sent_score and sent_score[sentence] >= (avg):
                summary += " " + sentence
        self.textEdit.setText(summary)

app = QApplication(sys.argv)
widget = MainPage()
widget.show()
sys.exit(app.exec_())