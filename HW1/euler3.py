# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

a = 600851475143
i = 2

while i * i <= a:
    while a % i == 0:
        a /= i
    i += 1
print(int(a))
