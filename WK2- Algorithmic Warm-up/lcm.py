# Uses python3
import sys

def lcm(a, b):
    if b==0:
    	return a
    else:
    	a_dash = a%b
    	return lcm(b,a_dash)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    prod = int((a*b) // (lcm(a,b))) 
    print(prod)

# a=14159572
# b=63967072
# prod = int((a*b) // (lcm(a,b)))
# print(prod)