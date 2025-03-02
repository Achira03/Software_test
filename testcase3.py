import unittest
def caesarCipher(s, k):
    ans = ''
    k = k % 26 
    for i in s:
        if i.islower():
            ans += chr(((ord(i) - ord('a') + k) % 26) + ord('a'))
        elif i.isupper():
            ans += chr(((ord(i) - ord('A') + k) % 26) + ord('A'))
        else:
            ans += i 
    return ans

class Test_caesarCipher(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(caesarCipher("abc", 1), "bcd")
        self.assertEqual(caesarCipher("xyz", 3), "abc")
        self.assertEqual(caesarCipher("Hello, World!", 0), "Hello, World!")
        self.assertEqual(caesarCipher("Hello, World!", 5), "Mjqqt, Btwqi!")
        self.assertEqual(caesarCipher("abc", 29), "def")
        self.assertEqual(caesarCipher("AbC", 2), "CdE")
        self.assertEqual(caesarCipher("def", -3), "abc")
        self.assertEqual(caesarCipher("", 5), "")

Test_caesarCipher()
print("All test cases passed!")