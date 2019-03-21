
s1 = ["i", "am", "a", "cat"]
s2 = ["a", "cat", "am", "i"]
s3 = ["i", "am", "the", "cat"]


class SentenceEdit:

    def __init__(self, source, target, postedit):

        self.source_sentence = source
        self.target_sentence = target
        self.post_edited_sentence = postedit

    def difference_within_word(self):
        pass

    def bag_of_words_diff(self):

        t = self.target_sentence
        t_ = self.post_edited_sentence

        tSet = set(t)
        t_Set = set(t_)

        if tSet != t_Set:
            return True
        else:
            return False

    def error_in_sequence(self):
        pass

    def error_in_tree(self):
        pass
