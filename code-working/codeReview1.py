def stable_marriage(men_preferences, women_preferences):
 
    free_men = list(men_preferences.keys())
    engagements = {} 
    men_proposals = {man: [] for man in men_preferences}

    while free_men:
        m = free_men[0] 
        m_prefs = men_preferences[m]


        for w in m_prefs:
            if w not in men_proposals[m]:
                men_proposals[m].append(w) 


                if w not in engagements:
                    engagements[w] = m
                    free_men.remove(m)
                    break
                else:
                    current_partner = engagements[w]
                    w_prefs = women_preferences[w]


                    if w_prefs.index(m) < w_prefs.index(current_partner):
                        engagements[w] = m
                        free_men.remove(m)
                        free_men.append(current_partner)
                        break


    return {(m, w) for w, m in engagements.items()}

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


