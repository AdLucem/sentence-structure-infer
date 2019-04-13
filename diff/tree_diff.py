class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def print_tree(tree):
    if tree == None: return
    if type(tree) is list:
        print (tree)
        return

    print_tree(tree.left)
    print (tree.cargo),
    print_tree(tree.right)

def diff(a, b):
    if a == None and b == None: return
    if a == None: return print_tree(b)
    if b == None: return print_tree(a)
    if type(a) is list and type(b) is list:
        if a == b: return
        else:
            print('tree 1:')
            print(list(set(a) - set(b)))
            print('tree 2:')
            print(list(set(b) - set(a)))
            return
    if (a.cargo == b.cargo):
        diff(a.left, b.left)
        diff(a.right, b.right)
    if (a.cargo != b.cargo):
        print('TREE 1:')
        print_tree(a)
        print('TREE 2:')
        print_tree(b)



def main():
    X = Tree('jumps', Tree('fox', ['The', 'quick', 'brown']), Tree('dog', ['over', 'the', 'lazy']))

    Y = Tree('jumps', Tree('fox', ['The', 'quick']), Tree('dog', ['over', 'the', 'lazy']))
    #print (X)
    #print_tree(X)
    diff(X,Y)
main()
