import unittest

def funnyString(s):
    n = len(s)
    for i in range(1, n):
        start_diff = abs(ord(s[i]) - ord(s[i - 1]))
        end_diff = abs(ord(s[n - i]) - ord(s[n - i - 1]))  # ใช้ s[n - i]
        if start_diff != end_diff:
            return 'Not Funny'
    return 'Funny'

class TestFunnyString(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(funnyString("acxz"), "Funny")
        self.assertEqual(funnyString("bcxz"), "Not Funny")
        self.assertEqual(funnyString("a"), "Funny")
        self.assertEqual(funnyString("aa"), "Funny")
        self.assertEqual(funnyString("ab"), "Funny")
        self.assertEqual(funnyString("racecar"), "Funny")
        self.assertEqual(funnyString("abcdefg"), "Funny")  # กรณีนี้ต้องเป็น "Not Funny"


