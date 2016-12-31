import timeit
st=timeit.default_timer()
out=[]
a=[1,648,558,14684,1654,51845,1554,615,461,659,149,199,4519,941,1649,451,9416,495668,51,9451,4,51,84,51694,19491,941,84]
for x in a:
	out.append(x)  
	out.sort()
print (out)
print(timeit.default_timer()-st) 

