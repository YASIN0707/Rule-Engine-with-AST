# app.py

from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)

# Route for creating a single rule and returning its AST representation
@app.route('/create_rule', methods=['POST'])
def create_rule_route():
    try:
        rule_string = request.json['rule']  # Extract rule from the request body
        ast = create_rule(rule_string)
        return jsonify({"message": "Rule created successfully", "ast": str(ast)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route for combining multiple rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules_route():
    try:
        rules = request.json.get('rules')  # Get the list of rules from the request body
        if not rules or len(rules) < 2:
            raise ValueError("You must provide at least two rules.")
        combined_ast = combine_rules(rules)
        return jsonify({"message": "Rules combined successfully", "combined_ast": str(combined_ast)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route for evaluating a rule against user data
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_route():
    try:
        data = request.get_json()
        ast = data.get('ast')
        user_data = data.get('data')

        if not ast or not user_data:
            return jsonify({"error": "Invalid data format."}), 400

        # Evaluate rule against the provided user data
        is_eligible = evaluate_rule(ast, user_data)
        return jsonify({"is_eligible": is_eligible}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)  # Default port 5000
