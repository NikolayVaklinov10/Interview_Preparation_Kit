import math

def checkBST(root):
    return checkBST_node(root, -math.inf, math.inf)

def checkBST_node(node,min,max):
    if node is None:
        return True
    else:
        return min < node.data < max \
                and checkBST_node(node.left, min, node.data)\
                and checkBST_node(node.right, node.data, max)
