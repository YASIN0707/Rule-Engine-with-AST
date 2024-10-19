// Mock API functions for demonstration
async function create_rule(ruleString) {
    return {
        type: 'root',
        left: { 
            type: 'operator', 
            value: 'AND', 
            left: { type: 'operand', value: ruleString } 
        },
        right: { 
            type: 'operand', 
            value: 'Some condition' 
        }
    };
}

async function combine_rules(ruleStrings) {
    // Mock combining rules (to be implemented in backend)
    // This function simulates combining multiple rules into a single AST.
    return {
        type: 'root',
        left: {
            type: 'operator',
            value: 'OR',
            left: { type: 'operand', value: ruleStrings[0] },
            right: { type: 'operand', value: ruleStrings[1] }
        },
        right: { 
            type: 'operand', 
            value: 'Combined conditions' 
        }
    };
}

async function evaluate_rule(ast, userData) {
    return true; // Mock evaluation (to be implemented in backend)
}

// DOM Elements
const createRuleButton = document.getElementById('createRuleButton');
const ruleStringInput = document.getElementById('ruleString');
const astOutput = document.getElementById('astOutput');
const combineRulesButton = document.getElementById('combineRulesButton');
const combineRulesInput = document.getElementById('combineRules');
const userDataInput = document.getElementById('userData');
const evaluateRuleButton = document.getElementById('evaluateRuleButton');
const evaluationOutput = document.getElementById('evaluationOutput');

// Event Listeners for creating a single rule
createRuleButton.addEventListener('click', async () => {
    const ruleString = ruleStringInput.value.trim();
    if (!ruleString) {
        alert("Please enter a valid rule.");
        return;
    }

    try {
        const ast = await create_rule(ruleString);
        astOutput.textContent = JSON.stringify(ast, null, 2);
    } catch (error) {
        console.error("Error creating rule:", error);
        alert("Failed to create rule.");
    }
});

// Event Listener for combining rules
combineRulesButton.addEventListener('click', async () => {
    const ruleStrings = combineRulesInput.value.trim().split('\n').map(line => line.trim()).filter(line => line);
    if (ruleStrings.length < 2) {
        alert("Please enter at least two rules to combine.");
        return;
    }

    try {
        const ast = await combine_rules(ruleStrings);
        astOutput.textContent = JSON.stringify(ast, null, 2);
    } catch (error) {
        console.error("Error combining rules:", error);
        alert("Failed to combine rules.");
    }
});

// Event Listener for evaluating the rule
evaluateRuleButton.addEventListener('click', async () => {
    const userDataString = userDataInput.value.trim();
    if (!userDataString) {
        alert("Please enter user data in JSON format.");
        return;
    }

    let userData;
    try {
        userData = JSON.parse(userDataString);
    } catch (error) {
        alert("Invalid JSON format for user data.");
        return;
    }

    let ast;
    try {
        ast = JSON.parse(astOutput.textContent); // Get AST from the output
    } catch (error) {
        alert("No valid AST found. Please create or combine rules first.");
        return;
    }

    try {
        const result = await evaluate_rule(ast, userData);
        evaluationOutput.textContent = `Evaluation Result: ${result}`;
    } catch (error) {
        console.error("Error evaluating rule:", error);
        evaluationOutput.textContent = "Failed to evaluate rule.";
    }
});
