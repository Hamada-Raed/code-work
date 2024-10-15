import math

# Class to hold chemical reaction data
class ChemicalReaction:
    def __init__(self, reaction_name, equilibrium_constant, reactant_concentration):
        self.reaction_name = reaction_name
        self.equilibrium_constant = equilibrium_constant
        self.reactant_concentration = reactant_concentration

# Function to calculate the combined equilibrium constant
def calculate_combined_equilibrium_constant(reactions):
    if not reactions:
        return None

    combined_constant = 1.0
    
    for reaction in reactions:
        product = math.prod(reaction.reactant_concentration)
        combined_constant *= reaction.equilibrium_constant ** product
    
    return combined_constant

# Input validation functions
def validate_float_input(value, min_val, max_val):
    try:
        float_value = float(value)
        if min_val <= float_value <= max_val:
            return float_value
    except ValueError:
        pass
    return None

def validate_non_empty(value):
    return value.strip() if value.strip() else None

# Read input from terminal and calculate combined equilibrium constant
num_reactions = validate_float_input(input("Enter the number of chemical reactions: "), 1, float('inf'))
if num_reactions is not None and num_reactions.is_integer():
    num_reactions = int(num_reactions)
    reactions = []
    is_valid_input = True
    
    for i in range(1, num_reactions + 1):
        reaction_name = validate_non_empty(input(f"Enter the name for reaction {i}: "))
        if reaction_name:
            equilibrium_constant = validate_float_input(input(f"Enter the equilibrium constant for reaction {i}: "), 0, 1e6)
            if equilibrium_constant is not None:
                num_reactants = validate_float_input(input(f"Enter the number of reactants for reaction {i}: "), 1, float('inf'))
                if num_reactants is not None and num_reactants.is_integer():
                    num_reactants = int(num_reactants)
                    concentrations = []
                    concentrations_valid = True
                    
                    for j in range(1, num_reactants + 1):
                        concentration = validate_float_input(input(f"Enter the concentration for reactant {j} (in mol/L): "), 0, 1e3)
                        if concentration is not None:
                            concentrations.append(concentration)
                        else:
                            print("Error: Concentration must be a number between 0 and 1000 mol/L.")
                            concentrations_valid = False
                            break
                    
                    if concentrations_valid:
                        reactions.append(ChemicalReaction(reaction_name, equilibrium_constant, concentrations))
                    else:
                        is_valid_input = False
                        break
                else:
                    print("Error: Number of reactants must be a positive integer.")
                    is_valid_input = False
                    break
            else:
                print("Error: Equilibrium constant must be a number between 0 and 1e6.")
                is_valid_input = False
                break
        else:
            print("Error: Reaction name cannot be empty.")
            is_valid_input = False
            break
    
    if is_valid_input:
        result = calculate_combined_equilibrium_constant(reactions)
        if result is not None:
            print(f"Combined Equilibrium Constant of the system: {result:.4e}")
        else:
            print("Error: Unable to calculate combined equilibrium constant.")
else:
    print("Error: Number of reactions must be a positive integer.")