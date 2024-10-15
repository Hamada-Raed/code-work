def stable_marriage(men_preferences, women_preferences):
    """
    Implements the Gale-Shapley algorithm to find stable matchings between men and women.

    Args:
        men_preferences (dict): A dictionary where keys are men's identifiers and values are lists of women's identifiers in order of preference.
        women_preferences (dict): A dictionary where keys are women's identifiers and values are lists of men's identifiers in order of preference.

    Returns:
        set: A set of tuples representing engaged pairs (man, woman).
    
    Raises:
        ValueError: If any man's or woman's preferences are empty or if there are mismatched participants.
    """
    # Input validation
    if not isinstance(men_preferences, dict) or not isinstance(women_preferences, dict):
        raise ValueError("Both men_preferences and women_preferences must be dictionaries.")

    if len(men_preferences) != len(women_preferences):
        raise ValueError("The number of men must equal the number of women.")

    for man, preferences in men_preferences.items():
        if not preferences or not all(w in women_preferences for w in preferences):
            raise ValueError(f"Invalid preferences for man {man}: {preferences}. Ensure they are non-empty and valid.")

    for woman, preferences in women_preferences.items():
        if not preferences or not all(m in men_preferences for m in preferences):
            raise ValueError(f"Invalid preferences for woman {woman}: {preferences}. Ensure they are non-empty and valid.")

    # Initialize all men and women as free
    free_men = list(men_preferences.keys())
    engagements = {}  # Dictionary to track engagements (woman -> man)
    men_proposals = {man: [] for man in men_preferences}  # Track proposals by each man

    while free_men:
        # Select the first free man
        m = free_men[0]
        m_prefs = men_preferences[m]

        # Iterate through the man's preference list
        for w in m_prefs:
            # Check if the man has already proposed to this woman
            if w not in men_proposals[m]:
                men_proposals[m].append(w)  # Record the proposal

                # If the woman is free, engage them
                if w not in engagements:
                    engagements[w] = m
                    free_men.remove(m)
                    break  # Exit the loop once engaged

                else:
                    # The woman is currently engaged; check her preference
                    current_partner = engagements[w]
                    w_prefs = women_preferences[w]

                    # Compare preferences and switch engagements if necessary
                    if w_prefs.index(m) < w_prefs.index(current_partner):
                        engagements[w] = m  # Update engagement
                        free_men.remove(m)  # Man is no longer free
                        free_men.append(current_partner)  # Former partner is now free
                        break  # Exit the loop after switching engagements

    # Return the set of engaged pairs
    return {(m, w) for w, m in engagements.items()}


# Example usage
if __name__ == "__main__":
    men_preferences = {
        'A': ['X', 'Y', 'Z'],
        'B': ['Y', 'X', 'Z'],
        'C': ['X', 'Y', 'Z'],
    }

    women_preferences = {
        'X': ['B', 'A', 'C'],
        'Y': ['A', 'B', 'C'],
        'Z': ['A', 'B', 'C'],
    }

    try:
        matches = stable_marriage(men_preferences, women_preferences)
        print("Engaged pairs:", matches)
    except ValueError as e:
        print("Error:", e)