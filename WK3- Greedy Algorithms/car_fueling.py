# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    start = 0
    end = distance
    stops.append(distance)
    refil = 0
    i = 0
    while(start<end and i<len(stops)):
        last_stop = start
        dist = stops[i]- start
        if (dist<=tank):
            i += 1
        elif(dist > tank):
            start = stops[i-1]
            if last_stop == start:
                return -1
            refil += 1
    return refil

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
