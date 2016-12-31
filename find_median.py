#using lambda function 
checkio=lambda d:(lambda t,n:t[n]+t[-n-1])(sorted(d),len(d)//2)/2