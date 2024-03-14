def LetterCountI(str):
    words = str.split()
    max_repeat = 0
    result = -1
    for word in words:
        char_dict = {}
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        repeat_count = max(char_dict.values())
        if repeat_count > max_repeat:
            max_repeat = repeat_count
            result = word
    return result

# Test Cases
print(LetterCountI("Today, is the greatest day ever!"))  # Output: greatest
print(LetterCountI("Are you ready for interview?"))      # Output: ready
print(LetterCountI("Nothing unusual here"))             # Output: unusaul
