def is_palindrome_iterative(word):  # type: ignore
    if not word:  # type: ignore
        return False

    word_length = len(word)

    return not any(word[i] != word[word_length - i - 1]
                   for i in range(word_length // 2))  # type: ignore
