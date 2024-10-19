# test_cases.py
from rule_engine import create_rule, combine_rules, evaluate_rule

def run_tests():
    try:
        print("Running Test 1: Simple rule with 'age > 30'")
        rule = create_rule("age > 30")
        data = {"age": 35}
        assert evaluate_rule(rule, data) == True
        print("Test 1 Passed")

        print("Running Test 2: Simple rule with 'salary > 50000' but no salary key in data")
        rule = create_rule("salary > 50000")
        data = {"age": 35}  # No salary key
        assert evaluate_rule(rule, data) == False  # Because salary defaults to 0
        print("Test 2 Passed")

        print("Running Test 3: Combined rule with AND operator")
        rule1 = create_rule("age > 30")
        rule2 = create_rule("salary > 50000")
        combined_rule = combine_rules(rule1, rule2, 'AND')
        data = {"age": 35, "salary": 60000}
        assert evaluate_rule(combined_rule, data) == True
        print("Test 3 Passed")

    except Exception as e:
        print("An error occurred:", e)

run_tests()
