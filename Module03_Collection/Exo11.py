
# list filter.
# Énoncé : Soit prix = [12, 55, 110]. Créer une liste des prix > 50 avec -10% en UNE ligne

print([int(e * 0.9) for e in [12, 55, 110] if e > 50])