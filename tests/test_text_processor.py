import unittest

from simphile import TextProcessor


class TestTextProcessor(unittest.TestCase):

    def test_tokenize(self):
        p = TextProcessor()
        # "a b" vs "a  b" vs "a b "
        self.assertListEqual(p.tokenize("a b"), p.tokenize("a  b"))
        self.assertListEqual(p.tokenize("a b"), p.tokenize("a b "))
        self.assertListEqual(p.tokenize("a b"), p.tokenize("a\nb"))
        self.assertListEqual(p.tokenize("a b"), p.tokenize("a\rb"))

    def test_process(self):
        p = TextProcessor(lowercase=True)
        self.assertEqual("a", p.process("A"))
        p = TextProcessor(only_alphabetic=True)
        self.assertEqual("a b", p.process("a*#$%^&.,/1b"))
