# generate n random numbers in certain range and save them to text file

import random

def main():
    # get user input
    n = int(input('How many random numbers do you want to generate? '))
    min = int(input('What is the minimum value? '))
    max = int(input('What is the maximum value? '))
    # generate random numbers and write to file
    with open('heights.txt', 'w') as f:
        for _ in range(n):
            f.write(str(random.randint(min, max)) + '\n')

# main guard
if __name__ == '__main__':
    main()