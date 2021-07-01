# encoding=utf-8

"""
HJ6 质数因子
"""

# Get input and initial prime number to 2
number_t = int(input())
prime_num = 2

if __name__ == '__main__':
    # Increase prime number and print it out if it match
    while(prime_num <= number_t):
        if number_t % prime_num == 0:
            print(prime_num, end=" ")
            number_t = number_t / prime_num
        else:
            prime_num = prime_num + 1
