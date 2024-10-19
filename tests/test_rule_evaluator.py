import unittest
from app.ast_builder import create_rule
from app.rule_evaluator import evaluate_rule

class TestRuleEvaluator(unittest.TestCase):

    def test_simple_rule(self):
        rule = "age > 30 AND department == 'Sales'"
        ast_node = create_rule(rule)
        data = {"age": 35, "department": "Sales"}
        self.assertTrue(evaluate_rule(ast_node, data))

    def test_complex_rule(self):
        rule = "(age > 30 AND department == 'Sales') OR (age < 25 AND department == 'Marketing')"
        ast_node = create_rule(rule)
        data = {"age": 23, "department": "Marketing"}
        self.assertTrue(evaluate_rule(ast_node, data))

if __name__ == '__main__':
    unittest.main()