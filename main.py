from linkedQ import LinkedQ, Syntaxfel
import unittest

"""
class SyntaxTest(unittest.TestCase):
    def testMole(self):
        self.assertEqual(check_mole("Aa5"), "Följer syntaxen!")

    def test2(self):
        self.assertEqual(check_mole("aa5"), "Saknad stor bokstav vid radslutet aa5")
"""
def check_mole(mole):
    q = LinkedQ()
    for char in mole:
        q.enqueue(char)

    try:
        read_atom(q)
    except Syntaxfel as e:
        remaining = []
        while not q.isEmpty():
            remaining.append(q.dequeue())
        left = ''.join(remaining)
        return f"{e} {left}"

    return "Formeln är syntaktiskt korrekt"

def read_atom(q):
    if q.isEmpty():
        return
    check_atom(q)
    if not q.isEmpty() and q.peek().isdigit():
        check_num(q)
    read_atom(q)


def check_atom(q):
    first_capital(q)
    if not q.isEmpty() and q.peek().islower():
        second_lower(q)

def first_capital(q):
    first = q.peek()
    if first.isupper():
        q.dequeue()
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

def second_lower(q):
    second = q.peek()
    if second.islower():
        q.dequeue()
    else:
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

def check_num(q):
    num = ""
    num += q.dequeue()

    if int(num) == 0:
        raise Syntaxfel("För litet tal vid radslutet")

    while not q.isEmpty() and q.peek().isdigit():
        num += q.dequeue()

    if int(num) < 2:
        raise Syntaxfel("För litet tal vid radslutet")

def main():
    while True:
        line = input()
        if line == "#":
            break
        print(check_mole(line))


if __name__ == '__main__':
    main()
    #unittest.main()