from node import Node

class Trie:
    """Class that controls the creation and basic Trie API"""
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.print_node(self.root, '')

    def print_node(self, node, string):
        if node is None:
            return string
        string = string + str(node)
        if node.left is not None:
            string = self.print_node(node.left, string)
        if node.mid is not None:
            string = self.print_node(node.mid, string)
        if node.right is not None:
            string = self.print_node(node.right, string)
        return string

    def put(self, key, value):
        self.root = self._put(self.root, key, value, 0)

    def _put(self, node, key, value, idx):
        char = key[idx]
        if node is None:
            node = Node()
            node.char = char
        if char < node.char:
            node.left = self._put(node.left, key, value, idx)
        elif char > node.char:
            node.right = self._put(node.right, key, value, idx)
        elif idx < len(key) - 1:
            node.mid = self._put(node.mid, key, value, idx + 1)
        else:
            node.value.append(value)
        return node
    
    def contains(self, key):
        return self.get(key) is not None

    def get(self, key):
        node = self._get(self.root, key, 0)
        if node is None:
            return None
        else:
            return node.value

    def _get(self, node, key, idx):
        if node is None:
            return None
        char = key[idx]
        if char < node.char:
            return self._get(node.left, key, idx)
        elif char > node.char:
            return self._get(node.right, key, idx)
        elif idx < len(key) - 1:
            return self._get(node.mid, key, idx + 1)
        else:
            return node

    def get_subtrie(self, key, N):
        node = self._get(self.root, key, 0)
        if node is None:
            return None
        else:
            # copy the contents to avoid modifying the value of the node
            children = list(node.value)
            if node.mid is not None:
                children = self.get_children(node.mid, N, children) 
            return children
