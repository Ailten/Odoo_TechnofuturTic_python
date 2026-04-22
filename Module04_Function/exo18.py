
# calculator with operator.
# Fonction calcul(a, b, op="+"). Gérer +, -, *, / et les erreurs d'opérateur inconnu.

def calcul(a: int, b: int, op: str='+'):  # can return float or int.
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
            if b == 0:
                raise ZeroDivisionError()
            return a / b
        case _:
            raise ValueError('operator unknow')
        
print(calcul(200, 200, '+'))
print(calcul(420, 20, '-'))
print(calcul(40, 10, '*'))
print(calcul(4000, 10, '/'))
#print(calcul(4000, 10, 'A'))

