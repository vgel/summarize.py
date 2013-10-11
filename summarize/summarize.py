#!/usr/bin/env python

import nltk
from nltk.corpus import stopwords
import string

stop_words = stopwords.words('english')

# The low end of shared words to consider
LOWER_BOUND = .20

# The high end, since anything above this is probably SEO garbage or a
# duplicate sentence
UPPER_BOUND = .90


def is_unimportant(word):
    """Decides if a word is ok to toss out for the sentence comparisons"""
    return word in ['.', '!', ',', ] or '\'' in word or word in stop_words


def only_important(sent):
    """Just a little wrapper to filter on is_unimportant"""
    return filter(lambda w: not is_unimportant(w), sent)


def compare_sents(sent1, sent2):
    """Compare two word-tokenized sentences for shared words"""
    if not len(sent1) or not len(sent2):
        return 0
    return len(set(only_important(sent1)) & set(only_important(sent2))) / ((len(sent1) + len(sent2)) / 2.0)


def compare_sents_bounded(sent1, sent2):
    """If the result of compare_sents is not between LOWER_BOUND and
    UPPER_BOUND, it returns 0 instead, so outliers don't mess with the sum"""
    cmpd = compare_sents(sent1, sent2)
    if cmpd <= LOWER_BOUND or cmpd >= UPPER_BOUND:
        return 0
    return cmpd


def compute_score(sent, sents):
    """Computes the average score of sent vs the other sentences (the result of
    sent vs itself isn't counted because it's 1, and that's above
    UPPER_BOUND)"""
    if not len(sent):
        return 0
    return sum(compare_sents_bounded(sent, sent1) for sent1 in sents) / float(len(sents))


def summarize_block(block):
    """Return the sentence that best summarizes block"""
    sents = nltk.sent_tokenize(block)
    word_sents = map(nltk.word_tokenize, sents)
    d = dict((compute_score(word_sent, word_sents), sent) for sent, word_sent in zip(sents, word_sents))
    return d[max(d.keys())]


def find_likely_body(b):
    """Find the tag with the most directly-descended <p> tags"""
    return max(b.find_all(), key=lambda t: len(t.find_all('p', recursive=False)))


class Summary(object):
    def __init__(self, url, article_html, title, summaries):
        self.url = url
        self.article_html = article_html
        self.title = title
        self.summaries = summaries

    def __repr__(self):
        return 'Summary({0}, {1}, {2}, {3})'.format(
            repr(self.url), repr(self.article_html), repr(self.title), repr(self.summaries)
        )

    def __str__(self):
        return u"{0} - {1}\n\n{2}".format(self.title, self.url, '\n'.join(self.summaries))


def summarize_page(url):
    import bs4
    import re
    import requests

    html = bs4.BeautifulSoup(requests.get(url).text)
    b = find_likely_body(html)
    summaries = map(lambda p: re.sub('\s+', ' ', summarize_block(p.text)).strip(), b.find_all('p'))
    summaries = sorted(set(summaries), key=summaries.index)  # deduplicate and preserve order
    summaries = [re.sub('\s+', ' ', summary.strip())
                 for summary in summaries
                 if filter(lambda c: c.lower() in string.letters, summary)]
    return Summary(url, b, html.title.text if html.title else None, summaries)

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 0:
        print u"%s" % summarize_page(sys.argv[1])
        sys.exit(0)

    print "Usage summarize.py <URL>"
    sys.exit(1)
