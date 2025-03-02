import unittest


def staircase(n, display):
    if n <= 0 or n > 30:
        return "n must be in the range of 1 to 30"
    
    result = []
    for i in range(1, n + 1):
        result.append(display * i)
    return '\n'.join(result)

class Teststaircase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(staircase(1, "#"), "#")
        self.assertEqual(staircase(4, "#"), "#\n##\n###\n####")
        self.assertEqual(staircase(5, "*"), "*\n**\n***\n****\n*****")
        self.assertEqual(staircase(30, "+"), "+\n++\n+++\n++++\n+++++\n" + "\n".join(["+" * i for i in range(6, 31)]))
        self.assertEqual(staircase(0, "#"), "n must be in the range of 1 to 30")
        self.assertEqual(staircase(-1, ""), "n must be in the range of 1 to 30")
        self.assertEqual(staircase(31, "+"), "n must be in the range of 1 to 30")
        self.assertEqual(staircase(100, ""), "n must be in the range of 1 to 30")
        self.assertEqual(staircase(5, "A"), "A\nAA\nAAA\nAAAA\nAAAAA")
        self.assertEqual(staircase(2, "@"), "@\n@@")

Teststaircase()
print("All test cases passed!")