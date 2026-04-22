
# calculator with operator.
# Fonction calcul(a, b, op="+"). Gérer +, -, *, / et les erreurs d'opérateur inconnu.

def calcul(a, b, op='+'):  # can return float or int.
    match op:
        case '+':
            return a + b
        case '*':
            return a * b
        case '-':
            return a - b
        case '+':
            return a + b
        case '/':
            return a / b
        case _:
            raise Exception('operator unknow')
        
print(calcul(200, 200, '+'))
print(calcul(420, 20, '-'))
print(calcul(40, 10, '*'))
print(calcul(4000, 10, '/'))
#print(calcul(4000, 10, 'A'))

