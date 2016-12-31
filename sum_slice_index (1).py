#c = lambda x:[ sum(x[::2]) * x[-1]]
#c([1,2,2,3,4,5)]
 
c = lambda x:sum(x[::2]*x[-1] if len(x)!=0 else int(0)
c([])