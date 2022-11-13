import sys

length = 50
pxwidth = 10

length = (length // 2) * 2 + 1

def help():
    print("A simple Python script for generating Ulam Spiral\n")
    print("Usage:")
    print(" python3 ulam.py <SPIRAL_WIDTH> <SQUARE_WIDTH> > <PPM_FILE_PATH>")
    print(" pypy3   ulam.py <SPIRAL_WIDTH> <SQUARE_WIDTH> > <PPM_FILE_PATH>")
    quit()

if len(sys.argv) != 3:
    help();
else:
    if sys.argv[1].isnumeric() == False or sys.argv[2].isnumeric() == False:
        help()
    else:
        length  = (int(sys.argv[1]) // 2) * 2 + 1
        pxwidth = int(sys.argv[2])

def sieve(n):
    arr = [*range(n+2)]
    arr[0] = arr[1] = 0
    for i in arr:
        if i > 1:
            for j in range(n//i-1):
                arr[i*(j+1)] = 0
            arr[i] = 1
    return arr

def main():

    vec = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]
    d = 0 ; x = 0 ; y = 0 ; z = 1 ; o = length//2
    mx = [[0 for x in range(length+1)] for x in range(length+1)]
    mx[o][o] = z
    for i in range(2*length):
        d = (d + 1) % 4
        for j in range(i//2+1):
            x += vec[d][0]
            y += vec[d][1]
            z += 1
            mx[y+o][x+o] = z
    isPrime = sieve(length**2+1)

    print("P3", length*pxwidth, length*pxwidth, 255)
    for i in range(length*pxwidth):
        for j in range(length*pxwidth):
            if isPrime[mx[i//pxwidth][j//pxwidth]]:
                if isPrime[mx[i//pxwidth][j//pxwidth]+2] or isPrime[mx[i//pxwidth][j//pxwidth]-2]:
                    # twin primes
                    print(0, 0, 0)
                else:
                    # normal primes
                    print(120, 120, 120)
            else:
                # composite numbers
                print(255,255,255)

main()

