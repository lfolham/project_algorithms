def is_palindrome_recursive(word, low_index=0, high_index=None):
    if not isinstance(word, str) or len(word) == 0:
        return False
    if high_index is None:
        high_index = len(word) - 1
    if low_index >= high_index:
        return True
    if word[low_index] != word[high_index]:
        return False
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
