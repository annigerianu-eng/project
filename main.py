n = int(input("Enter n: "))

# Step 1: create list of prime numbers from 1 to n
prime_list = []

for num in range(1, n + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)

# Step 2: create list of primes whose position is also prime
result = []

for index in range(len(prime_list)):
    if index > 1:
        is_prime_index = True
        for i in range(2, index):
            if index % i == 0:
                is_prime_index = False
                break
        if is_prime_index:
            result.append(prime_list[index])

print("Prime numbers from 1 to n:")
print(prime_list)

print("Prime numbers whose position is also prime:")
print(result)