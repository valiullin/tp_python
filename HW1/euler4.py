# coding: utf-8
# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

a, b = 100, 100
palindromic_max = 0
res = 0


while a <= 999:
    while b <= 999:
        res = a * b
        # if is_palindromic(res):
        if str(res) == str(res)[::-1]:
            if palindromic_max < res:
                palindromic_max = res
        b += 1
    b = 100
    a += 1

print(palindromic_max)
