import unittest


def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(list(grid[i]))
    for x in list(zip(*grid)):
        if list(x) != sorted(x):
            return "NO"
    return "YES"

class Test_gridChallenge(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(gridChallenge(["abc", "ade", "efg"]), "YES")
        self.assertEqual(gridChallenge(["abc", "ade", "efh"]), "YES")
        self.assertEqual(gridChallenge(["zxy"]), "YES")
        self.assertEqual(gridChallenge(["a", "b", "c"]), "YES")
        self.assertEqual(gridChallenge(["aaa", "aaa", "aaa"]), "YES")
        self.assertEqual(gridChallenge(["bac", "dca", "efg"]), "YES")
        self.assertEqual(gridChallenge([]), "YES")
        self.assertEqual(gridChallenge(["a"]), "YES")
        self.assertEqual(gridChallenge(["abc", "bcd", "ace"]), "NO")
        self.assertEqual(gridChallenge(["xyz", "wvu", "tsr"]), "NO")

Test_gridChallenge()
print("All test cases passed!")