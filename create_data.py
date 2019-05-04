from generic.read_data import Sentence


SENTENCE_FILE = "generated/templist.txt"
SRC_FILE = "data/eng-hin-src.txt"
MOD_FILE = "data/eng-hin-modified.txt"

data = Sentence.read_from_data(SRC_FILE, MOD_FILE)


ls = []
for obj in data:
    ls.append(obj.source)
    ls.append(obj.mt)
    ls.append(obj.postedit)
    ls.append("----------------------------------------")


with open("full_sentences.txt", "w+") as f:
    f.writelines(ls)