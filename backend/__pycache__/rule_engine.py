class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.left = left            # left child Node
        self.right = right          # right child Node
        self.value = value          # value for operand Nodes

    def __repr__(self):
        if self.node_type == 'operand':
            return f"{self.value}"
        return f"({self.left} {self.value} {self.right})"


def create_rule(rule_string):
    # A very basic implementation for creating an AST from a rule string.
    # This will need to be expanded to handle more complex rules.
    tokens = rule_string.replace("(", " ( ").replace(")", " ) ").split()
    return parse_expression(tokens)


def parse_expression(tokens):
    token = tokens.pop(0)
    if token == '(':
        left = parse_expression(tokens)
        operator = tokens.pop(0)
        right = parse_expression(tokens)
        tokens.pop(0)  # Remove the closing ')'
        return Node('operator', left, right, operator)
    else:
        return Node('operand', value=token)


def combine_rules(rules):
    combined_node = None
    for rule in rules:
        rule_node = create_rule(rule)
        if combined_node is None:
            combined_node = rule_node
        else:
            combined_node = Node('operator', combined_node, rule_node, 'AND')  # Combine with AND for simplicity
    return combined_node


def evaluate_rule(ast, user_data):
    if ast.node_type == 'operand':
        # Simple comparison implementation
        left = ast.value.split()[0]
        operator = ast.value.split()[1]
        right = ast.value.split()[2].strip("'")  # Remove quotes from string values

        if left in user_data:
            if operator == '>':
                return user_data[left] > int(right)
            elif operator == '<':
                return user_data[left] < int(right)
            elif operator == '=':
                return user_data[left] == right
    elif ast.node_type == 'operator':
        left_result = evaluate_rule(ast.left, user_data)
        right_result = evaluate_rule(ast.right, user_data)
        if ast.value == 'AND':
            return left_result and right_result
        elif ast.value == 'OR':
            return left_result or right_result

    return False
