import numpy as np
import pymorphy3
import nltk
from joblib import load
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
word_to_index = load('A:\\Users\Artem\PycharmProjects\kafkaTest\ML\\telecom_V4_word_to_index.joblib')
punctuation_marks = ['!', ',', '(', ')', ':', '-', '?', '.', '..', '...', '"', '\'', '«', '»', ';', '–', '--', '``',
                     '`']
stop_words = stopwords.words("russian")
morph = pymorphy3.MorphAnalyzer()


def preprocess(text, stop_words=stop_words, punctuation_marks=punctuation_marks, morph=morph):
    tokens = word_tokenize(text.lower())
    preprocessed_text = []
    for token in tokens:
        if token not in punctuation_marks:
            lemma = morph.parse(token)[0].normal_form
            if lemma not in stop_words:
                preprocessed_text.append(lemma)
    return preprocessed_text


def text_to_sequence(txt, word_to_index=word_to_index):
    seq = []
    for word in txt:
        index = word_to_index.get(word, 1)  # 1 означает неизвестное слово
        # Неизвестные слова не добавляем в выходную последовательность
        if index != 1:
            seq.append(index)
    return seq
