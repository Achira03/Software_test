import unittest

def alternatingCharacters(s):
    d=0
    sl=list(s)
    for i in range(0, len(sl)-1):
        if sl[i]==sl[i+1]:
            d+=1
    return d

class Test_alternatingCharacters(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("AABB"), 2)
        self.assertEqual(alternatingCharacters("ABABABAAB"), 1)
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters(""), 0)
        self.assertEqual(alternatingCharacters("AB" * 1000), 0)
        self.assertEqual(alternatingCharacters("A" * 1000), 999)

Test_alternatingCharacters
print("All test cases passed!")