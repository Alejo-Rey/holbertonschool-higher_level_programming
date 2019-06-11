#!/usr/bin/python3
''' testitn Square '''
import unittest
from models.square import Square


class testId(unittest.TestCase):
    ''' class to test '''

    def test_Base(self):
        n = Square(5)
        self.assertEqual(n.area(), 25)
