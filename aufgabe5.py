def vereinfachter_ausdruck(a, b):
    left_side = (not a or not b) * (not a or b) * (a or not b)
    right_side = (not a or b) * (a or not b)
    return left_side == right_side
a = True
b = False
ergebnis = vereinfachter_ausdruck(a, b)
print("Ergebnis des vereinfachten Ausdrucks:", ergebnis)


def vereinfachte_disjunktion(x, y, z):
    return (x or (y and z)) == ((x or y) and (x or z))
x = True
y = False
z = True
ergebnis = vereinfachte_disjunktion(x, y, z)
print("Ergebnis der vereinfachten Disjunktion:", ergebnis)


def vereinfachte_konjunktion(x, y, z):
    return (x and (y or z)) == ((x and y) or (x and z))
x = True
y = False
z = True
ergebnis = vereinfachte_konjunktion(x, y, z)
print("Ergebnis der vereinfachten Konjunktion:", ergebnis)
      

def vereinfachter_ausdruck(a, b):
    return (a or b) and (not a or b) and (a or not b) and (not a or not b)
a = True
b = False
ergebnis = vereinfachter_ausdruck(a, b)
print("Ergebnis des vereinfachten Ausdrucks:", ergebnis)


def vereinfachter_ausdruck(b, a):
    return (not b) or a
b = True
a = False
ergebnis = vereinfachter_ausdruck(b, a)
print("Ergebnis des vereinfachten Ausdrucks:", ergebnis)

def vereinfachter_ausdruck(a, b):
    return a and (not b)
a = True
b = False
ergebnis = vereinfachter_ausdruck(a, b)
print("Ergebnis des vereinfachten Ausdrucks:", ergebnis)


def vereinfachter_ausdruck(c, d):
    return c or d
c = True
d = False
ergebnis = vereinfachter_ausdruck(c, d)
print("Ergebnis des vereinfachten Ausdrucks:", ergebnis)


def vereinfachter_ausdruck(a, b, c, nu):
    return (not a or not b or not c) and (not a or nu or not c)
a = True
b = False
c = True
nu = False
ergebnis = vereinfachter_ausdruck(a, b, c, nu)
print("Ergebnis des vereinfachten Ausdrucks:", ergebnis)

def vereinfachter_ausdruck(a, c):
    return a and c
a = True
c = False
ergebnis = vereinfachter_ausdruck(a, c)
print("Ergebnis des vereinfachten Ausdrucks:", ergebnis)