import random


def guess_number():
    secret = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            guess = int(input("Ваш вариант: "))
            attempts += 1
            if guess == secret:
                print(f"Поздравляю! Вы угадали число за {attempts} попыток!")
                break
            elif guess < secret:
                print("Слишком мало!")
            else:
                print("Слишком много!")
        except ValueError:
            print("Введите целое число!")


if __name__ == "__main__":
    guess_number()