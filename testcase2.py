def alternatingCharacters(s):
    d=0
    sl=list(s)
    for i in range(0, len(sl)-1):
        if sl[i]==sl[i+1]:
            d+=1
    return d

def test_alternatingCharacters():
    assert alternatingCharacters("ABABABAB") == 0    
    assert alternatingCharacters("AAAA") == 3
    assert alternatingCharacters("AABB") == 2
    assert alternatingCharacters("ABABABAAB") == 1
    assert alternatingCharacters("A") == 0
    assert alternatingCharacters("") == 0
    assert alternatingCharacters("AB" * 1000) == 0
    assert alternatingCharacters("A" * 1000) == 999

test_alternatingCharacters()
print("All test cases passed!")