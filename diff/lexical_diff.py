
class LexicalDiff:
    """Differentiates two sentences purely in terms of
    the words in them, regardless of word position."""

    def __init__(self, source, target):

        self.source = source
        self.target = target
        self.words_removed = []
        self.words_added = []

    def get_words_removed(self):

        src = self.source
        tgt = self.target

        for i in range(len(src)):
            word = src[i]
            if word not in tgt:
                self.words_removed.append(i)

    def get_words_added(self):

        src = self.source
        tgt = self.target

        for i in range(len(tgt)):
            word = tgt[i]
            if word not in src:
                self.words_added.append(i)

    def display(self):

        src = self.source
        tgt = self.target
        rem = self.words_removed
        add = self.words_added

        for i in range(len(src)):
            word = src[i]
            if i in rem:
                print "(" + word + ") ",
            else:
                print word + " ",
        print
        for j in range(len(tgt)):
            word = tgt[j]
            if j in add:
                print "(" + word + ") ",
            else:
                print word + " ",
