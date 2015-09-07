class Node:
    """Auxiliary class to be used within the Trie"""
    def __init__(self):
        self.value = []
        self.char = None
        self.left = None
        self.mid = None
        self.right = None
    
    def __str__(self):
        string = self.char + '[' + ' '.join(self.value) + '], ' 
        if self.left != None:
            string = string + self.left.char
        string = string + ', '
        if self.mid != None:
            string = string + self.mid.char
        string = string + ', '
        if self.right != None:
            string = string + self.right.char
        string = string + '\n'
        return string
