# ==================== Setting Up System Encoding ======================

"""This should remain at the top of the main.py file"""
#import sys
#import importlib
#importlib.reload(sys)
#sys.setdefaultencoding('utf-8')

# ======================================================================

from generic.read_data import Sentence
from chunk.dep_tree import DepTree
from chunk.dep_chunk import dep_chunk
#from utils.utils import hindi_corpus_tokenize
#from lexical_diff import LexicalDiff
import re

SENTENCE_FILE = "generated/templist.txt"

data = Sentence.read_sentence_file(SENTENCE_FILE)

for obj in data:
    mod = re.sub(r"[A-Za-z()]", "", obj.postedit)
    mt = obj.mt
    
    deps_mt = obj.mt_dep_parse()
    deps_mod = obj.mod_dep_parse()

    tree_mt = DepTree()
    tree_mt.make_tree(deps_mt)
    tree_mod = DepTree()
    tree_mod.make_tree(deps_mod)

    head_mt_index = tree_mt.tree[0].children[0]
    head_mod_index = tree_mod.tree[0].children[0]

    head_mt = tree_mt.tree[head_mt_index].word 
    head_mod = tree_mod.tree[head_mod_index].word
    
    print(str(head_mt) + "  " + str(head_mod))
    #print(tree_mod.test_tree(deps_mod))
    #chunks = dep_chunk(tree)
    #print(chunks)

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
