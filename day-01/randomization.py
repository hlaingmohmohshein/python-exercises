import random
import my_module
random_integer = random.randrange(1,10)
# print(my_module.pi)
print('Random number from 0 to 1 :', random.random())
print('Uniform Distribution between [1,5] :', random.uniform(1, 5))
print('Gaussian Distribution with mean = 0 and standard deviation = 1 :', random.gauss(0, 1))
print('Exponential Distribution with lambda = 0.1 :', random.expovariate(0.1))
print('Normal Distribution with mean = 1 and standard deviation = 2:', random.normalvariate(1, 5))
