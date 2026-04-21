
# inverted dico.
#Soit d = {"a": 1, "b": 2}. Créer un nouveau dictionnaire d_inv = {1: "a", 2: "b"} via une compréhension.

d = {"a": 1, "b": 2}

d2 = { v: k for k, v in d.items() }

print(d)
print(d2)