#!/usr/bin/python3
''' testing Rectangle '''
import unittest
from models.rectangle import Rectangle


class testId(unittest.TestCase):
    ''' class to test '''

    def test_Base(self):
        n = Rectangle(4, 5)
        self.assertEqual(n.area(), 20)
