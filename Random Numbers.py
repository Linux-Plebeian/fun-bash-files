import time
import random
a = random.randint(1, 10)
print('Here\'s a random number')
time.sleep(1)
print(random.randint(1, 1000000000))
time.sleep(1)
for i in range(a):
    print('Here\'s another random number')
    time.sleep(1)
    print(random.randint(1, 1000000000))
    time.sleep(1)
print(f'That makes {a + 1} randomly generated numbers!')
