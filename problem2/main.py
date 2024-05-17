def bilangan_prima(n):
    if n < 2 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primeX(x):
    prime_numbers = [2]
    num = 3
    while len(prime_numbers) < x:
        if bilangan_prima(num):
            prime_numbers.append(num)
        num += 2
    return prime_numbers[-1]

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29