def fibonacci(number):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, number + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[number]

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144