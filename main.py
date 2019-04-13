# ==================== Setting Up System Encoding ======================

"""This should remain at the top of the main.py file"""
#import sys
#import importlib
#importlib.reload(sys)
#sys.setdefaultencoding('utf-8')

# ======================================================================

from generic.read_data import Sentence
#from utils.utils import hindi_corpus_tokenize
#from lexical_diff import LexicalDiff

SENTENCE_FILE = "generated/templist.txt"

data = Sentence.read_sentence_file(SENTENCE_FILE)
example = data[0].postedit

Sentence.get_deps(example)

#print(data[0].mt_dep_parse())
#print(data[0].mod_dep_parse())


"""
MT_CORPUS = "data/eng-hin-mt.txt"
MODIFIED_CORPUS = "data/eng-hin-modified.txt"
n = 10

# take the mt corpus and divide it into sentences
mt = hindi_corpus_tokenize(MT_CORPUS, n)
mod = hindi_corpus_tokenize(MODIFIED_CORPUS, n)

# for each sentence
for i in range(n):
    src = mt[i]
    tgt = mod[i]

    # take a lexical diff of it
    diff = LexicalDiff(src, tgt)
    diff.get_words_removed()
    diff.get_words_added()

    # display the diff
    diff.display()
    print
    print "-----------------------------------------"
"""
