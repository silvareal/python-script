def reverses(text):
    return text[: :-1]
def is_palindrome(text):
    return text==reverses(text)

something = input("enter text:")
if is_palindrome(something):
    print("is palindrome")
else:
    print("not palindrome")
