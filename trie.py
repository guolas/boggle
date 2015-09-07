from node import Node

class Trie:
    """Class that controls the creation and basic Trie API"""
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.print_node(self.root, '')

    def print_node(self, node, string):
        if node == None:
            return string
        string = string + str(node)
        if node.left != None:
            string = self.print_node(node.left, string)
        if node.mid != None:
            string = self.print_node(node.mid, string)
        if node.right != None:
            string = self.print_node(node.right, string)
        return string

    def put(self, key, value):
        self.root = self.put_inner(self.root, key, value, 0)

    def put_inner(self, node, key, value, idx):
        char = key[idx]
        if node == None:
            node = Node()
            node.char = char
        if char < node.char:
            node.left = self.put_inner(node.left, key, value, idx)
        elif char > node.char:
            node.right = self.put_inner(node.right, key, value, idx)
        elif idx < len(key) - 1:
            node.mid = self.put_inner(node.mid, key, value, idx + 1)
        else:
            node.value.append(value)
        return node
    
    def contains(self, key):
        return self.get(key) != None

    def get(self, key):
        node = self.get_inner(self.root, key, 0)
        if node == None:
            return None
        else:
            return node.value

    def get_inner(self, node, key, idx):
        if node == None:
            return None
        char = key[idx]
        if char < node.char:
            return self.get_inner(node.left, key, idx)
        elif char > node.char:
            return self.get_inner(node.right, key, idx)
        elif idx < len(key) - 1:
            return self.get_inner(node.mid, key, idx + 1)
        else:
            return node

    def get_subtrie(self, key, N):
        node = self.get_inner(self.root, key, 0)
        if node == None:
            return None
        else:
            # copy the contents to avoid modifying the value of the node
            children = list(node.value)
            if node.mid != None:
                children = self.get_children(node.mid, N, children) 
            return children
