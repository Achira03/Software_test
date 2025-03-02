def funnyString(s):
    n = len(s)
    for i in range(1, n):
        start_diff = abs(ord(s[i]) - ord(s[i - 1]))
        end_diff = abs(ord(s[n - i] ) - ord(s[n - i - 1]))  # ใช้ s[n - i]
        if start_diff != end_diff:
            return 'Not Funny'
    return 'Funny'

def test_funnyString():
    assert funnyString("acxz") == "Funny"
    assert funnyString("bcxz") == "Not Funny"
    assert funnyString("a") == "Funny"
    assert funnyString("aa") == "Funny"
    assert funnyString("ab") == "Funny"
    assert funnyString("racecar") == "Funny"
    assert funnyString("abcdefg") == "Funny"

test_funnyString()
print("All test cases passed!")