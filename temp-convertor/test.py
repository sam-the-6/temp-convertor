from unittest import TestCase
from temperature import main


class TestConsole(TestCase):
    def test_basic(self):
        main()
