from unittest import TestCase
from temperature import Temp


class TestConsole(TestCase):
    def test_basic(self):
        self.assertEqual(Temp.calc(1, 'f'), None)
