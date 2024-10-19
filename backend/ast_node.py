# ast_node.py

class Node:
    def __init__(self, type, value=None):
        self.type = type  # 'operator' or 'operand'
        self.value = value  # e.g., 'AND', 'age > 30', etc.
        self.left = None  # Left child node (for operators)
        self.right = None  # Right child node (for operators)
