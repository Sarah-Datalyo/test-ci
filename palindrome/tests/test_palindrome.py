import unittest
from palindrome.palindrome import is_palindrome_new


class PalindromeTest(unittest.TestCase):

    # Liste des tests: le nom du tests doit commencer par test_ pour qu'il soit reconnu par PyCharm

    def test_is_palindrome(self):  # méthode de tests de la fonction say_hello
        self.assertEqual(is_palindrome_new("world"), False)
        self.assertEqual(is_palindrome_new("kayak"), True)