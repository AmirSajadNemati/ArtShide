import random

def random_number_by_digits_generator(N):
    minimum = pow(10, N - 1)
    maximum = pow(10, N) - 1
    return random.randint(minimum, maximum)



