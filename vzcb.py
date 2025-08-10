import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Генератор случайных паролей")
    try:
        length = int(input("Введите длину пароля (8-20): "))
        if 8 <= length <= 20:
            print(f"Ваш пароль: {generate_password(length)}")
        else:
            print("Длина должна быть от 8 до 20 символов!")
    except ValueError:
        print("Введите целое число!")

if __name__ == "__main__":
    main()