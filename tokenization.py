# from nltk.tokenize import word_tokenize

# def tokenize(sent):
#     return word_tokenize(sent)

import re

def tokenize(text):
    return re.findall(r'\b\w+\b', text)
