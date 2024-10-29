const readline = require("readline");
const fs = require("fs");

// Setup readline interface for user input in Node.js
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to get user input and return a promise for async handling
function askQuestion(query) {
    return new Promise(resolve => rl.question(query, answer => resolve(answer)));
}

// Class to hold chemical reaction data
class ChemicalReaction {
    constructor(reactionName, equilibriumConstant, reactantConcentration) {
        this.reactionName = reactionName;
        this.equilibriumConstant = equilibriumConstant;
        this.reactantConcentration = reactantConcentration;
    }
}

// Function to calculate the combined equilibrium constant
function calculateCombinedEquilibriumConstant(reactions) {
    if (!reactions.length) return null;

    let combinedConstant = 1.0;

    reactions.forEach(reaction => {
        const product = reaction.reactantConcentration.reduce((acc, val) => acc * val, 1);
        combinedConstant *= Math.pow(reaction.equilibriumConstant, product);
    });

    return combinedConstant;
}

// Input validation functions
function validateFloatInput(value, minVal, maxVal) {
    const floatValue = parseFloat(value);
    return (!isNaN(floatValue) && floatValue >= minVal && floatValue <= maxVal) ? floatValue : null;
}

function validateNonEmpty(value) {
    return value.trim() ? value.trim() : null;
}

// Function to save reactions to a file
function saveReactionsToFile(reactions, result) {
    const data = {
        reactions: reactions.map(reaction => ({
            name: reaction.reactionName,
            equilibriumConstant: reaction.equilibriumConstant,
            reactantConcentration: reaction.reactantConcentration
        })),
        combinedEquilibriumConstant: result
    };
    fs.writeFileSync("reactions_data.json", JSON.stringify(data, null, 2));
    console.log("Data saved to reactions_data.json.");
}

// Function to load and display saved reactions from file
function displaySavedReactions() {
    if (fs.existsSync("reactions_data.json")) {
        const data = JSON.parse(fs.readFileSync("reactions_data.json", "utf-8"));
        console.log("\nSaved Reactions Data:");
        console.log(JSON.stringify(data, null, 2));
    } else {
        console.log("\nNo saved reaction data found.");
    }
}

// Main function to handle user input for chemical reactions
async function handleReactionsInput() {
    let numReactions = validateFloatInput(await askQuestion("Enter the number of chemical reactions: "), 1, Infinity);
    if (numReactions && Number.isInteger(numReactions)) {
        let reactions = [];
        let isValidInput = true;

        for (let i = 1; i <= numReactions; i++) {
            let reactionName = validateNonEmpty(await askQuestion(`Enter the name for reaction ${i}: `));
            if (reactionName) {
                let equilibriumConstant = validateFloatInput(await askQuestion(`Enter the equilibrium constant for reaction ${i}: `), 0, 1e6);
                if (equilibriumConstant !== null) {
                    let numReactants = validateFloatInput(await askQuestion(`Enter the number of reactants for reaction ${i}: `), 1, Infinity);
                    if (numReactants && Number.isInteger(numReactants)) {
                        let concentrations = [];
                        let concentrationsValid = true;

                        for (let j = 1; j <= numReactants; j++) {
                            let concentration = validateFloatInput(await askQuestion(`Enter the concentration for reactant ${j} (in mol/L): `), 0, 1e3);
                            if (concentration !== null) {
                                concentrations.push(concentration);
                            } else {
                                console.log("Error: Concentration must be a number between 0 and 1000 mol/L.");
                                concentrationsValid = false;
                                break;
                            }
                        }

                        if (concentrationsValid) {
                            reactions.push(new ChemicalReaction(reactionName, equilibriumConstant, concentrations));
                        } else {
                            isValidInput = false;
                            break;
                        }
                    } else {
                        console.log("Error: Number of reactants must be a positive integer.");
                        isValidInput = false;
                        break;
                    }
                } else {
                    console.log("Error: Equilibrium constant must be a number between 0 and 1e6.");
                    isValidInput = false;
                    break;
                }
            } else {
                console.log("Error: Reaction name cannot be empty.");
                isValidInput = false;
                break;
            }
        }

        if (isValidInput) {
            const result = calculateCombinedEquilibriumConstant(reactions);
            if (result !== null) {
                console.log(`Combined Equilibrium Constant of the system: ${result.toExponential(4)}`);
                saveReactionsToFile(reactions, result);
            } else {
                console.log("Error: Unable to calculate combined equilibrium constant.");
            }
        }
    } else {
        console.log("Error: Number of reactions must be a positive integer.");
    }
}

// Interactive menu function
async function interactiveMenu() {
    while (true) {
        console.log("\nMenu:");
        console.log("1. Enter new chemical reactions");
        console.log("2. View saved reactions");
        console.log("3. Exit");
        const choice = await askQuestion("Choose an option: ");

        if (choice === "1") {
            await handleReactionsInput();
        } else if (choice === "2") {
            displaySavedReactions();
        } else if (choice === "3") {
            console.log("Exiting program.");
            rl.close();
            break;
        } else {
            console.log("Invalid choice. Please select an option from the menu.");
        }
    }
}

interactiveMenu();
