

def get_attr_number(node):
    s = 0
    if node is not None:
        s += len(node.attrib)
        for child in node:
            s += get_attr_number(child)
    return s

