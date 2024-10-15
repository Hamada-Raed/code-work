def stable_marriage(men_preferences, women_preferences):
    # Initialize the list of free men and engagements
    free_men = list(men_preferences.keys())
    engagements = {}
    men_proposals = {man: set() for man in men_preferences}  # Use a set for faster lookup

    while free_men:
        man = free_men[0]
        man_prefs = men_preferences[man]

        for woman in man_prefs:
            if woman not in men_proposals[man]:
                men_proposals[man].add(woman)  # Add to set for O(1) complexity

                if woman not in engagements:
                    # Woman is free, engage her with the man
                    engagements[woman] = man
                    free_men.remove(man)
                    break
                else:
                    # Woman is already engaged, check if she prefers this man
                    current_partner = engagements[woman]
                    woman_prefs = women_preferences[woman]

                    if woman_prefs.index(man) < woman_prefs.index(current_partner):
                        # Woman prefers the new man, switch engagements
                        engagements[woman] = man
                        free_men.remove(man)
                        free_men.append(current_partner)
                        break

    return {(man, woman) for woman, man in engagements.items()}

# Example usage
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

matches = stable_marriage(men_preferences, women_preferences)
print("Engaged pairs:", matches)