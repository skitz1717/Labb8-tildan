from linkedQ import LinkedQ, Syntaxfel

def check_mole(mole):
    q = LinkedQ()
    for char in mole:
        q.enqueue(char)

    try:
        read_atom(q)
        return "Formeln är syntaktiskt korrekt"
    except Syntaxfel as error:
        remaining = []
        while not q.isEmpty():
            remaining.append(q.dequeue())
        left = ''.join(remaining)
        return f"{error} {left}"

def read_atom(q):
    if q.isEmpty():
        return
    check_atom(q)
    if not q.isEmpty() and q.peek().isdigit():
        check_num(q)
    read_atom(q)


def check_atom(q):
    first_capital(q)
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
        return


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
