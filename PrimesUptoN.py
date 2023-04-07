import time
from math import sqrt

# input Number

print("Enter Number: ")
N = int(input())

# Program exicution begins
start_time = time.time()


def printPrimeUptoN(N):
    if N == 0 or N == 1:
        print('Not Prime')
        return

    elif N == 2:
        print(2)
        return

    elif N>2 and N<=1000000:

        # Low range

        if N < 100:
            queue = []
            for num in range(2, N + 1):
                for i in range(2, (num // 2) + 1):
                    if num % i == 0:
                        break
                else:
                    queue.append(num)
            print(queue)
            return
        else:
            # High range i.e., N>99
            # limiting divisor range for memory optimisation

            queue = []
            for num in range(2, N + 1):
                for i in range(2, int(sqrt(N))):
                    if num in [2,3,5,7]:
                        continue
                    if num % i == 0:
                        break
                else:
                    queue.append(num)
            print(queue)
            return
    else:
        time.sleep(1)
        for i in range(10):
            print("I'm not a supercomputer. Please enter a smaller number")


printPrimeUptoN(N)

# Program runtime in milliseconds
end_time = time.time()
print('Runtime', round((end_time - start_time)*1000,4), 'ms')
