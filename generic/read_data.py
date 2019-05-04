import stanfordnlp
import re

from generic.read_anu import translate


class Sentence:

    nlp = stanfordnlp.Pipeline(lang="hi")

    def __init__(self, src, mt, mod):

        self.source = src
        self.mt = mt
        self.postedit = Sentence.clean_postedit(mod)

    @staticmethod
    def clean_postedit(sent):
        """Remove english words from the postedited sentences"""
        sent = re.sub(r'[A-Za-z]', "", sent)
        return sent

    def display(self):

        print("========")
        print(self.source)
        print("--------")
        print(self.mt)
        print("--------")
        print(self.postedit)
        print("========")

    @staticmethod
    def read_sentence_file(filename):

        with open(filename, "r+") as f:
            s = f.readlines()

        num_lines = len(s)
        sentences = []
        for i in range(0, num_lines, 3):
            src, mt, mod = s[i], s[i+1], s[i+2]
            new_sent = Sentence(src, mt, mod)
            sentences.append(new_sent)

        return sentences

    @staticmethod
    def read_from_data(src_file, mod_file):

        with open(src_file, "r+") as f:
            src_sents = f.readlines()
        with open(mod_file, "r+") as f:
            mod_sents = f.readlines()

        num_lines = len(src_sents)
        sentences = []
        for i in range(0, num_lines):
            src = src_sents[i]

            if len(src) > 200:
                continue

            mt = translate(src)
            mod = mod_sents[i]
            new_sent = Sentence(src, mt, mod)
            sentences.append(new_sent)

        return sentences



    @staticmethod
    def print_deps(sentence):

        doc = Sentence.nlp(sentence)
        s = doc.sentences
        s[0].print_dependencies()

    def mt_dep_parse(self):

        mt_doc = Sentence.nlp(self.mt)
        s = mt_doc.sentences
        return s[0].dependencies

    def mod_dep_parse(self):

        postedit_doc = Sentence.nlp(self.postedit)
        s = postedit_doc.sentences
        return s[0].dependencies

