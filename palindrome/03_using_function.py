def check_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"


check = check_palindrome("python")

print(check)
