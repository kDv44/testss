def is_palindrome(text):
    return text == text[::-1]


def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
