def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def main():
    user_input = input("Введите строку для проверки на палиндром: ")
    if is_palindrome(user_input):
        print("Это палиндром!")
    else:
        print("Это не палиндром!")

if __name__ == "__main__":
    main()