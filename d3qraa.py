def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_up_to_n(n):
    return [num for num in range(2, n + 1) if is_prime(num)]

def main():
    try:
        n = int(input("Введите число до которого искать простые числа: "))
        if n < 2:
            print("Введите число больше 1!")
        else:
            primes = get_primes_up_to_n(n)
            print(f"Простые числа до {n}: {primes}")
            print(f"Количество простых чисел: {len(primes)}")
    except ValueError:
        print("Введите целое число!")

if __name__ == "__main__":
    main()