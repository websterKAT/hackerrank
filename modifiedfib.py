# Enter your code here. Read input from STDIN. Print output to STDOUT
t1,t2,n = raw_input().strip().split(' ')
t1,t2,n = [int(t1),int(t2),int(n)]
fib = {1:t1,2:t2}
for k in range(3,n+1):
	f = fib[k-2] + (fib[k-1])**2
	fib[k] = f
print(fib[k])