import random

def roll_dice(num_dice=2, sides=6):
    results = [random.randint(1, sides) for _ in range(num_dice)]
    return results

def main():
    print("Симулятор броска кубиков")
    try:
        num_dice = int(input("Сколько кубиков бросить? (1-5): "))
        if 1 <= num_dice <= 5:
            results = roll_dice(num_dice)
            print(f"Результаты броска: {results}")
            print(f"Сумма: {sum(results)}")
        else:
            print("Введите число от 1 до 5!")
    except ValueError:
        print("Введите целое число!")

if __name__ == "__main__":
    main()