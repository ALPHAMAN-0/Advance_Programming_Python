total = 0

for number in range(2, 1000):
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        total += number

print("Sum of all primes below 1000 is:", total)
