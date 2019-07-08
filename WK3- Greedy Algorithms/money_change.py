# Uses python3
import sys

def get_change(m):
    n = m
    coins = 0
    while(n>=10):
        n -= 10
        coins += 1
    #find the number of coins with 5 denomination
    while(n>=5):
        n -= 5
        coins += 1
    #find the number of coins with 1 denomination
    while(n>=1):
        n -= 1
        coins+=1
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
