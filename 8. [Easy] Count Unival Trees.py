This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1


To start off, we should go through some examples.

  a
 / \
a   a
    /\
   a  a
       \
        A

This tree has 3 unival subtrees: the two 'a' leaves, and the one 'A' leaf. The 'A' leaf causes all its parents to not be counted as a unival tree.

  a
 / \
c   b
    /\
   b  b
        \
         b

This tree has 5 unival subtrees: the leaf at 'c', and every 'b'.

We can start off by first writing a function that checks whether a tree is unival or not. Then, perhaps we could use this to count up all the nodes in the tree.

To check whether a tree is a unival tree, we must check that every node in the tree has the same value. To start off, we could define an is_unival function that takes in a root to a tree. We would do this recursively with a helper function. Recall that a leaf qualifies as a unival tree.

def is_unival(root):
    return unival_helper(root, root.value)

def unival_helper(root, value):
    if root is None:
        return True
    if root.value == value:
        return unival_helper(root.left, value) and unival_helper(root.right, value)
    return False
    
def count_unival_subtrees(root):
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return 1 + left + right if is_unival(root) else left + right

# n = Node(0)
# n.left = Node(1)
# n.right = Node(0)
# n.right.left = Node(1)
# n.right.left.left = Node(1)
# n.right.left.right = Node(1)
# n.right.right = Node(0)

# n = Node('a')
# n.left = Node('a')
# n.right = Node('a')
# n.right.left = Node('a')
# n.right.right = Node('a')
# n.right.right.right = Node('A')

# n = Node('a')
# n.left = Node('a')
# n.right = Node('a')
# n.right.left = Node('a')
# n.right.right = Node('a')
# n.right.right.right = Node('A')
# n.right.right.right.left = Node('A')
# n.right.right.right.right = Node('A')

# n = Node('a')
# n.left = Node('c')
# n.right = Node('b')
# n.right.left = Node('b')
# n.right.right = Node('b')
# n.right.right.right = Node('b')

class Node:
    def __init__(self,n):
        self.val = n
        self.left = None
        self.right = None
        
n = Node('a')
n.left = Node('a')
n.right = Node('a')
n.right.left = Node('a')
n.right.right = Node('a')
n.right.right.right = Node('A')

def parseTree(node):
    if node and node.left and node.right:
        cntUniValLeft, isUniValLeft = parseTree(node.left)
        cntUniValRight, isUniValRight = parseTree(node.right)
        
        if node.left.val == node.right.val == node.val and isUniValLeft and isUniValRight:
            return 1 + cntUniValLeft + cntUniValRight, True
        else:
            return cntUniValLeft + cntUniValRight, False
    else:
        if node.left:
            cntUniValLeft, isUniValLeft = parseTree(node.left)
            if node.val == node.left.val and isUniValLeft:
                return 1 + cntUniValLeft, True
            else:
                return cntUniValLeft, False
        elif node.right:
            cntUniValRight, isUniValRight = parseTree(node.right)
            if node.val == node.right.val and isUniValRight:
                return 1 + cntUniValRight, True
            else:
                return cntUniValRight, False
        else:
            return 1, True
    
ans = parseTree(n)[0]