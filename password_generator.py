import random

x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = 8

a = "".join(random.sample(x,length))

print(a)