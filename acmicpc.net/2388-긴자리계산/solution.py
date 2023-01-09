import sys
a, b = map(lambda v: int(v.strip()), sys.stdin.readlines())
print(a+b, a-b, a*b, sep='\n')
