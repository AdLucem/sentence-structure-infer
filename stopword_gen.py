# -*- encoding: utf-8 -*-

from HindiTokenizer import Tokenizer
from utils import sent_tokenize


def unigrammatize(sequence):
    unigrams = {}

    for word in sequence:
        if word not in unigrams:
            unigrams[word] = 1
        else:
            unigrams[word] += 1

    return unigrams


def freq_sorted_unigrams(unigrams):
    unigrams_ = []
    for key in sorted(unigrams, key=unigrams.get, reverse=True):
        unigrams_.append((key, unigrams[key]))

    return unigrams_


def show_unigrams(unigrams):

    for unit in unigrams:
        print unit[0].decode("utf-8"),
        print unit[1]


if __name__ == "__main__":

    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

    # define the delimiter
    danda_ = int("0964", 16)
    delim = unichr(danda_)

    # read in the data
    f = open("data/eng-hin-modified.txt", "r+")
    s = f.readlines()
    f.close()

    sentences = []

    # tokenize the whole thing into sentences
    for line in s[1:2000]:
        t_ = sent_tokenize(line, delim)
        t_ = [x for x in t_ if x != "\n"]
        sentences += t_

    # tokenize the whole thing into words
    words = []
    for sent in sentences:
        tok_ = Tokenizer(sent)
        tok_.tokenize()
        words += tok_.tokens

    unigrams = unigrammatize(words)
    unigrams = freq_sorted_unigrams(unigrams)

    #stopwords = []
    for gram in unigrams:
        print gram[0].decode("utf-8")
    #    if gram[1] > 270:
    #        stopwords.append(gram[0])
    #    else:
    #        break
    #for stop in stopwords:
    #    print stop.decode("utf-8")
