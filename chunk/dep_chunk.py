
def dep_chunk(dep_obj):

    tree = dep_obj.tree
    root = tree[0]
    heads = root.children

    chunk_heads = []
    for head_index in heads:
        chunk_heads.extend(tree[head_index].children)

    chunks = []
    for head in chunk_heads:
        head_node = tree[head]

        # iterate down the tree
        chunks.append(head_node.word)

    return chunks

