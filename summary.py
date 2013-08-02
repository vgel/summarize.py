#!/usr/bin/env python

import itertools
import nltk
from nltk.corpus import stopwords
import string

stop_words = stopwords.words('english')

LOWER_BOUND = .20 #The low end of shared words to consider
UPPER_BOUND = .90  #The high end, since anything above this is probably SEO garbage or a duplicate sentence

def is_unimportant(word):
    return word in ['.', '!', ',', ] or '\'' in word or word in stop_words

def only_important(sent):
    return filter(lambda w: not is_unimportant(w), sent)

def compare_sents(sent1, sent2):
    """Compare two word-tokenized sentences for shared words"""
    if not len(sent1) or not len(sent2):
        return 0
    return len(set(only_important(sent1)) & set(only_important(sent2))) / ((len(sent1) + len(sent2)) / 2.0)

def compare_sents_bounded(sent1, sent2):
    cmpd = compare_sents(sent1, sent2)
    if cmpd <= LOWER_BOUND or cmpd >= UPPER_BOUND:
        return 0
    return cmpd

def compute_score(sent, sents):
    if not len(sent):
        return 0
    return sum( compare_sents_bounded(sent, sent1) for sent1 in sents ) / float(len(sent))

def summarize_block(block):
    sents = nltk.sent_tokenize(block)
    word_sents = map(nltk.word_tokenize, sents)
    d = dict( (compute_score(word_sent, word_sents), sent) for sent, word_sent in zip(sents, word_sents) )
    return d[max(d.keys())]

def summarize_page(url):
    import bs4
    import re
    import requests

    b = bs4.BeautifulSoup(requests.get(url).text)
    summaries = map(lambda p: re.sub('\s+', ' ', summarize_block(p.text)).strip(), b.find_all('p'))
    summaries = sorted(set(summaries), key=summaries.index) #dedpulicate and preserve order
    for summary in list(summaries):
        if not len(filter(lambda c: c.lower() in string.letters, summary)):
            summaries.remove(summary)
    print '\n\n'.join(summaries)

if __name__ == '__main__':
    import sys
    summarize_page(sys.argv[1])