#Uses Python3

import sys

def gcd_euclidean(a, b):
	if b==0:
		return a
	else:
		a_dash = a%b
		return gcd_euclidean(b,a_dash)
	

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_euclidean(a, b))

