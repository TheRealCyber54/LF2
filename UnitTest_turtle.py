import unittest
from turtle import *

class TestTurtle(unittest.TestCase):
    def test_PreisEntfernung(self):
        self.assertAlmostEqual(preisEntfernung(5), 4.45)

    def test_PreisMinuten(self):
        self.assertAlmostEqual(preisMinuten(5), 1.05)