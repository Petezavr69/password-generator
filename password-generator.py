import random

print('|Passwords Generator|')
while True:
    chars = list('+-/*!&$#?=w@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    length = int(input('Length Password?'+ "\n"))
    random.shuffle(chars)
    pasw = ''.join([random.choice(chars) for x in range(length)])
    print(f'Your Password - {pasw}')
