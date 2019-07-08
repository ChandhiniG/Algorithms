#Uses python3

def fib(n):
	l =[]
	l.append(0)
	if n==0:
		return l[n]
	l.append(1)
	if n==1:
		return l[n]
	else:
		for i in range(2,n+1):
			sum = (l[i-1]%10)+(l[i-2]%10)
			l.append(sum%10)
	return (l[n])

n = int(input())
print(fib(n))
