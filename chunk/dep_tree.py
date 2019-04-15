import copy

class DepNode:
    """To read stanfordnlp's dependency
    format into one we can manipulate"""

    def __init__(self, word, parent):

        self.word = word
        self.parent = parent
        self.children = []

    def add_child(self, child_index):

        self.children.append(child_index)


class DepTree:
    """Note: implementing the dependency tree
    as a dictionary of {index : node}, purely for
    personal convenience."""

    def __init__(self):
        self.tree = {}

    def make_tree(self, deps):

        for arc in deps:
            head, word = arc[0], arc[2]
            head_index, word_index = int(head.index), int(word.index)

            """Adding word to the tree"""

            # making a new node from the word, if word doesn't already exist
            if word_index not in self.tree:
                new_node = DepNode(word.text, head_index)
                # adding the word to the tree
                self.tree[word_index] = new_node
            # else, add the parent index to the word
            else:
                self.tree[word_index].parent = head_index

            """Adding word as child to parent node"""

            # if parent node already exists
            if head_index in self.tree:
                # add it to children of parent node
                self.tree[head_index].add_child(word_index)
            # else create parent node with unknown parent of itself
            else:
                p_node = DepNode(head.text, -1)
                p_node.add_child(word_index)
                self.tree[head_index] = p_node

    def test_tree(self, deps):

        # TODO: will eat memory if I run this on a large corpus
        # write a memory-efficient tree formation testing function
        # that is, if I ever get around to rewriting this code
        # which is not likely after NLA project ends
        temp_tree = copy.deepcopy(self.tree)
        test = True
        for node_index in temp_tree:

            node = temp_tree[node_index]
            temp_ch = node.children

            for arc in deps:
                head_index, word_index = int(arc[0].index), int(arc[2].index)

                if node_index == head_index:
                    if word_index not in temp_ch:
                        test = False
                    elif word_index in temp_ch:
                        temp_ch.remove(word_index)

            if len(temp_ch) > 0:
                test = False

        return test

    def show_tree(self):

        def print_node(index):
        
            s = " ( " + str(index)

            for i in self.tree[index].children:
                s += print_node(i) + " ) "

            return s

        return print_node(0) + " ) "

    def test_print_tree(self):

        for i in self.tree:
            print(str(i) + " : " + str(self.tree[i].children))

#    @staticmethod
#    def get_subtree(index):

        