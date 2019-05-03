


def dep_chunk(dep_obj, level=0):

    tree = dep_obj.tree
    root = tree[0]
    heads = root.children

    chunk_heads = []
    for head_index in heads:
        chunk_heads.extend(tree[head_index].children)

    chunks = []

    # get level one heads
    sub_heads = []
    indices = {}
    for head in chunk_heads:
        sub_heads.append(tree[head].word)
        indices[tree[head].word] = head

    if level == 0:

        for index, head in enumerate(sub_heads):
            if head in ("", []):
                sub_heads.pop(index)

        return sub_heads, indices

    if level == 1:
        # get level one heads
        l1_heads = []
        l1_indices = {}
        for subhead in sub_heads:

            children = tree[indices[subhead]].children

            for ch_index in children:
                l1_heads.append(tree[ch_index].word)
                l1_indices[tree[ch_index].word] = ch_index

        for index, head in enumerate(l1_heads):
            if head in ("", []):
                l1_heads.pop(index)

        return l1_heads, l1_indices
