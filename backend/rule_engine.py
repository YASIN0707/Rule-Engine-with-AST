# rule_engine.py

class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # Can be "operator" or "comparison"
        self.value = value      # Holds the actual condition for comparison nodes
        self.left = left        # Left child for operator nodes
        self.right = right      # Right child for operator nodes

    def __repr__(self):
        if self.type == 'comparison':
            return f'({self.value})'
        return f'({self.left} {self.value} {self.right})'


def create_rule(rule_string):
    # Parse a rule string and return an AST (this is a simplified parser)
    # We will only parse very simple rules here for the sake of example
    if 'AND' in rule_string:
        left_part, right_part = rule_string.split(' AND ')
        return Node('operator', 'AND', create_rule(left_part.strip()), create_rule(right_part.strip()))
    elif 'OR' in rule_string:
        left_part, right_part = rule_string.split(' OR ')
        return Node('operator', 'OR', create_rule(left_part.strip()), create_rule(right_part.strip()))
    else:
        # It's a leaf node - a condition like "age > 30"
        return Node('comparison', value=rule_string)


def combine_rules(rules):
    # Combine two or more rules into a single AST (by default combining using AND)
    if len(rules) < 2:
        raise ValueError("You must provide at least two rules to combine.")
    
    combined_ast = create_rule(rules[0])  # Start with the first rule
    for rule in rules[1:]:
        new_ast = create_rule(rule)
        combined_ast = Node('operator', 'AND', combined_ast, new_ast)

    return combined_ast


def evaluate_rule(ast, user_data):
    if ast.type == 'comparison':
        # Evaluate the condition by parsing the value in the AST
        return eval(ast.value, {}, user_data)
    elif ast.type == 'operator':
        if ast.value == 'AND':
            return evaluate_rule(ast.left, user_data) and evaluate_rule(ast.right, user_data)
        elif ast.value == 'OR':
            return evaluate_rule(ast.left, user_data) or evaluate_rule(ast.right, user_data)
    return False
