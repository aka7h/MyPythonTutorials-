def euclid(x1,x2,y1,y2):
	dis1 = x1-y1
	dis2 = x2-y2
	dis = (dis1**2) + (dis2**2)
	d = dis**(1/2)
	print ("The euclid distance is %.2f" % d)

euclid(-1, -1, -3, -3)
