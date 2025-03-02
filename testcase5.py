def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = sorted(list(grid[i]))
    for x in list(zip(*grid)):
        if list(x) != sorted(x):
            return "NO"
    return "YES"

def test_gridChallenge():
    assert gridChallenge(["abc", "ade", "efg"]) == "YES"
    assert gridChallenge(["abc", "ade", "efh"]) == "YES"
    assert gridChallenge(["zxy"]) == "YES"
    assert gridChallenge(["a", "b", "c"]) == "YES"
    assert gridChallenge(["aaa", "aaa", "aaa"]) == "YES"
    assert gridChallenge(["bac", "dca", "efg"]) == "YES"
    assert gridChallenge([]) == "YES"
    assert gridChallenge(["a"]) == "YES"
    assert gridChallenge(["abc", "bcd", "ace"]) == "NO"
    assert gridChallenge(["xyz", "wvu", "tsr"]) == "NO"

test_gridChallenge()
print("All test cases passed!")