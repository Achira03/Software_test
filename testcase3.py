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

def test_caesarCipher():
    assert caesarCipher("abc", 1) == "bcd"    
    assert caesarCipher("xyz", 3) == "abc"
    assert caesarCipher("Hello, World!", 0) == "Hello, World!"
    assert caesarCipher("Hello, World!", 5) == "Mjqqt, Btwqi!"
    assert caesarCipher("abc", 29) == "def"
    assert caesarCipher("AbC", 2) == "CdE"
    assert caesarCipher("def", -3) == "abc"
    assert caesarCipher("", 5) == ""

test_caesarCipher()
print("All test cases passed!")