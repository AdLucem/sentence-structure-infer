
from HindiTokenizer import Tokenizer


def hindi_corpus_tokenize(filename, n):
    """Take an entire hindi corpus- indicated by a single
    filename- and return a list of lists of tokens.
    Reads in the first 'n' lines of a corpus only."""

    # define the delimiter
    danda_ = int("0964", 16)
    delim = unichr(danda_)

    with open(filename, "r+") as f:
        s = f.readlines()

    # tokenize the whole thing into sentences
    sentences = []
    for line in s[0:n]:
        t_ = sent_tokenize(line, delim)
        t_ = [x for x in t_ if x != "\n"]
        sentences += t_

    # tokenize the whole thing into words
    words = []
    for sent in sentences:
        tok_ = Tokenizer(sent)
        tok_.tokenize()
        tok_ = remove_english_tokens(tok_.tokens)
        words.append(tok_)

    return words


def sent_tokenize(paragraph, delim):
    """Tokenizes a paragraph into sentences according
    to a given delimiter"""

    lines = []
    line = ""
    paragraph = paragraph.decode("utf-8", "ignore")

    for i in paragraph:

        if i == delim:
            lines.append(line)
            line = ""
        else:
            line += i

    if line != "":
        lines.append(line)

    return lines


def tokenize_sentence(sent):
    """Takes a sentence as input and returns a list of tokens"""

    tok_ = Tokenizer(sent)
    tok_.tokenize()
    return tok_.tokens


def remove_english_tokens(tokens): 
    """Takes a list of hindi/english tokens and removes the english
    tokens. Also removes punctuation."""

    clean = [t for t in tokens if not t.isalpha()]
    return clean
