import unittest
from unittest import TestCase


class TestActivityLog(TestCase):
    def setUp(self) -> None:
        print("hi")

    def test_is_this_working(self):
        print("1")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_is_this_working_2(self):
        print("2")
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
