from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)

# Route to create a rule and return its AST representation
@app.route('/create_rule', methods=['POST'])
def api_create_rule():
    data = request.json
    rule_string = data.get('rule_string')

    # Check if rule_string is provided
    if not rule_string:
        return jsonify({"error": "Missing rule_string"}), 400

    # Create the rule and return the AST as a response
    try:
        ast = create_rule(rule_string)
        return jsonify({"ast": str(ast)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to combine multiple rules into a single AST
@app.route('/combine_rules', methods=['POST'])
def api_combine_rules():
    data = request.json
    rules = data.get('rules')

    # Check if rules are provided
    if not rules:
        return jsonify({"error": "Missing rules list"}), 400

    # Combine the rules and return the combined AST
    try:
        combined_ast = combine_rules(rules)
        return jsonify({"combined_ast": str(combined_ast)}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to evaluate a rule against user data
@app.route('/evaluate_rule', methods=['POST'])
def api_evaluate_rule():
    data = request.json
    ast_string = data.get('ast_string')
    user_data = data.get('user_data')

    # Check if AST string and user data are provided
    if not ast_string or not user_data:
        return jsonify({"error": "Missing ast_string or user_data"}), 400

    try:
        # Create the AST from the provided string
        ast = create_rule(ast_string)  # Ensure your create_rule can handle this
        # Evaluate the rule against the user data
        result = evaluate_rule(ast, user_data)
        return jsonify({"result": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)
