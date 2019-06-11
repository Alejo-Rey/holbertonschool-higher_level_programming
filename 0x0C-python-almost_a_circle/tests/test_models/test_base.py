#!/usr/bin/python3
''' testitn Base '''
import unittest
from models.base import Base


class testId(unittest.TestCase):
    ''' class to test '''

    def test_Base(self):
        n = Base()
        self.assertEqual(n.id, 1)
