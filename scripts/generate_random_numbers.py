# generate 100 random numbers between INT_MIN and INT_MAX
# and write them to a file

import random

INT_MIN = -2147483648
INT_MAX = 2147483647

def main():
    with open('random_numbers.txt', 'w') as f:
        for i in range(100):
            f.write(str(i*10) + '\n')

# main guard
if __name__ == '__main__':
    main()
        