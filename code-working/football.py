# def parse_formation(formation):
#     try:
#         return list(map(int, formation.split('-')))
#     except ValueError:
#         raise ValueError("Formation is not valid. Use format 'X-X-X'.")

# def generate_positions(formation):
#     # Coordinates where players are placed for each type of role
#     # Y-axis placement:
#     goal_y = 0
#     defense_y = 20
#     midfield_y = 50
#     attack_y = 80

#     # X-axis spreads
#     # Assuming a standard pitch width of 100 units
#     field_width = 100

#     # Begin with the goalkeeper
#     players_positions = [("Goalkeeper", (field_width // 2, goal_y))]

#     defender_count, midfielder_count, forward_count = formation

#     # Calculate defender positions along the X-axis
#     defender_positions = [
#         ("Defender", (x, defense_y))
#         for x in range(field_width // (defender_count + 1), field_width, field_width // (defender_count + 1))
#     ]

#     # Calculate midfielder positions along the X-axis
#     midfielder_positions = [
#         ("Midfielder", (x, midfield_y))
#         for x in range(field_width // (midfielder_count + 1), field_width, field_width // (midfielder_count + 1))
#     ]

#     # Calculate forward positions along the X-axis
#     forward_positions = [
#         ("Forward", (x, attack_y))
#         for x in range(field_width // (forward_count + 1), field_width, field_width // (forward_count + 1))
#     ]

#     # Append all positions to the players list
#     players_positions.extend(defender_positions)
#     players_positions.extend(midfielder_positions)
#     players_positions.extend(forward_positions)

#     return players_positions

# def print_player_positions(players_positions):
#     for player, position in players_positions:
#         print(f"{player}: Position {position}")

# def simulate_formation(formation):
#     try:
#         formation_list = parse_formation(formation)
#         if len(formation_list) not in {3}:
#             raise ValueError("Unsupported formation format; should have exactly three numbers.")
        
#         players_positions = generate_positions(formation_list)
#         print_player_positions(players_positions)

#     except ValueError as e:
#         print(f"Error: {e}")

# # Example usage:
# formations_to_test = ["4-4-2", "3-5-2", "4-3-3"]

# for formation in formations_to_test:
#     print(f"\nSimulating formation: {formation}")
#     simulate_formation(formation) 

def get_positions(formation):

#Given a formation string like "4-4-2", returns the player positions on the pitch.

# Define pitch dimensions

	pitch_length = 100

	pitch_width = 60

# Parse the formation input to get the number of players in each line

	try:
		defense, midfield, attack = map(int, formation.split('-'))

	except ValueError:	
		print("Invalid formation format. Please use a format like '4-4-2'.")

	return

# Ensure the formation adds up to 10 outfield players

	total_players = defense + midfield + attack

	if total_players != 10:
		print("Invalid formation. Total outfield players must be 10.")

	return

# Goalkeeper position (fixed)

	positions = [("Goalkeeper", (5, pitch_width // 2))]

# Calculate positions for defenders

	defense_y_positions = [

	(i + 1) * (pitch_width // (defense + 1)) for i in range(defense)

	]

	for i, y in enumerate(defense_y_positions):
		positions.append((f"Defender {i + 1}", (25, y)))

# Calculate positions for midfielders

	midfield_y_positions = [

	(i + 1) * (pitch_width // (midfield + 1)) for i in range(midfield)

	]

	for i, y in enumerate(midfield_y_positions):
		positions.append((f"Midfielder {i + 1}", (50, y)))

# Calculate positions for forwards

	attack_y_positions = [

	(i + 1) * (pitch_width // (attack + 1)) for i in range(attack)

	]

	for i, y in enumerate(attack_y_positions):
		positions.append((f"Forward {i + 1}", (75, y)))

# Output player positions

	print(f"Formation: {formation}")

	for role, (x, y) in positions:
		print(f"{role}: Position ({x}, {y})")

def main():

# Test the program with three common formations

    formations = ["4-4-2", "3-5-2", "4-3-3"]

    for formation in formations:
        print("\n----------------------------------------")

    get_positions(formation)

    print("----------------------------------------\n")

if __name__ == "__main__":
	main()
