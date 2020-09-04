import math
user_num = int(input("Upper limit for prime: "))


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)): # check this number is prime or not divide by 2 to root of this number
        if num % i == 0: # if the number is divide by any number within 2 to root of this number then return false and this number is not Prime
            return False
    return True  # after the loop if there are no False case then its return True means this number is prime


for i in range(1,user_num):  # print all of the prime number from 1 to this number
    if is_prime(i):
        print(i)
