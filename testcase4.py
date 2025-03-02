import unittest

def alternate(s):
    lens = [0]
    letters = list(set(list(s)))
    for letter1 in range(len(letters)):
        for letter2 in range(letter1 + 1, len(letters)):
            two = []
            for letter in s:
                if letter == letters[letter1]:
                    if two:
                        if two[-1] == letters[letter2]:
                            two.append(letter)
                        else:
                            two = []
                            break
                    else:
                        two.append(letter)
                elif letter == letters[letter2]:
                    if two:
                        if two[-1] == letters[letter1]:
                            two.append(letter)
                        else:
                            two = []
                            break
                    else:
                        two.append(letter)
            lens.append(len(two))
    return max(lens)

class Test_alternate(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(alternate("beabeefeab"), 5)  # "babab" or "ababa"
        self.assertEqual(alternate("aaaa"), 0)
        self.assertEqual(alternate("abcde"), 2)  # "ab" or "bc" or "cd" or "de"
        self.assertEqual(alternate("ababab"), 6)
        self.assertEqual(alternate("a"), 0)
        self.assertEqual(alternate(""), 0)
        self.assertEqual(alternate("abababababababababab"), 20)
        self.assertEqual(alternate("aaaaaaaaaaaaaaaaaaaa"), 0)

Test_alternate()
print("All test cases passed!")