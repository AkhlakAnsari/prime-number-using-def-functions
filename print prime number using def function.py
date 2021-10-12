#print prime number using def function
print ( 'PRIME NUMBER' )
def prime_number(number):
    for first_prime_number in range ( 1, number + 1 ):
        count = 0
        for second_prime_number in range ( 1, first_prime_number + 1 ):
            if (first_prime_number % second_prime_number == 0):
                count = count + 1
        if count == 2:
            print ( first_prime_number )
prime_number(100)

#thanks akhlakansari94@gmail.com