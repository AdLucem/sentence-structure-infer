from generic.read_data import Sentence
from diff.lexical_diff import LexicalDiff
from chunk.dep_tree import DepTree
from chunk.dep_chunk import dep_chunk
from utils.utils import all_match

import re

SENTENCE_FILE = "generated/templist.txt"
SRC_FILE = "data/eng-hin-mt.txt"
MOD_FILE = "data/eng-hin-modified.txt"

#data = Sentence.read_from_data(SRC_FILE, MOD_FILE)
data = Sentence.read_sentence_file(SENTENCE_FILE)

for obj in data:

    deps_mt = obj.mt_dep_parse()
    deps_mod = obj.mod_dep_parse()

    tree_mt = DepTree()
    tree_mt.make_tree(deps_mt)
    tree_mod = DepTree()
    tree_mod.make_tree(deps_mod)

    chunks_mt, ind_mt = dep_chunk(tree_mt)
    chunks_mod, ind_mod = dep_chunk(tree_mod)

    while (len(chunks_mt) > 0) and (len(chunks_mod) > 0):
        chunks, cl = all_match(chunks_mt, chunks_mod)
        if cl == 0:
            break

        src = chunks[0]
        tgt = chunks[1]
        srcChunk = tree_mt.get_subtree(ind_mt[src])
        tgtChunk = tree_mod.get_subtree(ind_mod[tgt])

        diff = LexicalDiff(srcChunk, tgtChunk)
        diff.get_words_removed()
        diff.get_words_added()

        diff.display()
        print("\n+++++++++++++++++++++++++++++++++++++++")
        chunks_mt.remove(chunks[0])
        chunks_mod.remove(chunks[1])

    print("\n===========================================")



"""
-----------------------------------------------------
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
