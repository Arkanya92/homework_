def is_prime(func):
    def wrappers(*args, **kwargs):
        n = func(*args, **kwargs)
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")

        return n
    return wrappers

@is_prime
def sum_three(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum


result = sum_three(4, 6, 3, 2, 5)
print(result)