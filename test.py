from main import *
import unittest

class SyntaxTest(unittest.TestCase):
    def testMole(self):
        self.assertEqual(check_mole("Aa5"), "Formeln är syntaktiskt korrekt")

    def test2(self):
        self.assertEqual(check_mole("aa5"), "Saknad stor bokstav vid radslutet aa5")

if __name__ == '__main__':
    unittest.main()
