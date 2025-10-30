class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, x):
        """
        Lägger till en ny nod i slutet av länkade listan och sätter nästa nod till None
        Om listan är tom så sker ett specialfall annars kommer alltid else satsen att köras
        :param x: Värdet som ska stoppas in i noden
        :return:
        """
        new = Node(x)
        new.next = None
        if self.first is None:
            self.first = new
            self.last = new
        else:
            self.last.next = new
            self.last = new

    def dequeue(self):
        """
        Tar bort första elementet ur länkade listan och flyttar sedan efter pekaren för
        första och sista elementet
        :return: Om listan inte är tom returneras värde annars returneras ingenting
        """
        if self.isEmpty() is False:
            value = self.first.value
            if self.first == self.last:
                self.first = None
                self.last = None
            else:
                self.first = self.first.next
            return value
        else:
            return None

    def isEmpty(self):
        """
        Kollar om länkade listan är tom eller inte
        :return: True eller False
        """
        if self.first is None and self.last is None:
            return True
        else:
            return False

    def peek(self):
        if not self.isEmpty():
            return self.first.value
        else:
            return None

class Syntaxfel(Exception):
    pass


