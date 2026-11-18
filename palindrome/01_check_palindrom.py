word = input("Enter a word: ").lower()

reversed_word = word[::-1]

if word == reversed_word:
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")
