def is_prime(func):
    def wrapper(*args, ** kwargs):
        sum_three = func(*args, **kwargs)
        if sum_three > 1:
            for i in range(2, int(sum_three ** 0.5) + 1):
                if sum_three % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")
        return sum_three
    return wrapper


@is_prime
def sum_three(*abc):
    return sum(abc)

result = sum_three(2, 3, 6)
print(result)

result2 = sum_three(2,4,6)
print(result2)