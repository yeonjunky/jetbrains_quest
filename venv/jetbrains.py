def is_prime_number(x):

    if x <= 0:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True

prime_number = []

for i in range(500, 5001):
    if is_prime_number(i) == True:
        prime_number.append(i)

print(len(prime_number))
#https://jb.gg/574