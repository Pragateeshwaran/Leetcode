def count_equal_unique_splits_backtracking(S: str) -> int:
    """
    Counts the number of ways to split the string S into two non-empty substrings S1 and S2
    such that the number of unique characters in S1 is equal to the number of unique characters in S2.
    This implementation uses a backtracking approach.
    
    Parameters:
    - S (str): The input string to be split.
    
    Returns:
    - int: The number of valid split ways.
    
    Examples:
    >>> count_equal_unique_splits_backtracking("aaaa")
    3
    >>> count_equal_unique_splits_backtracking("bac")
    0
    >>> count_equal_unique_splits_backtracking("ababa")
    2
    """
    


if __name__ == "__main__":
    test_cases = [
        ("aaaa", 3),
        ("bac", 0),
        ("ababa", 2),
        
    ]
    
    for s, expected in test_cases:
        result = count_equal_unique_splits_backtracking(s)
        print(f"Input: '{s}' | Expected: {expected} | Got: {result}")
        assert result == expected, f"Test failed for input: '{s}'"
    
    print("All tests passed!")