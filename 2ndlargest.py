max1=int(input()) 
max2=None
while True:
    cur = int(input())
    if(cur == -1): break
    if(cur > max1):
        max2=max1
        max1=cur
    elif(cur<=max1 and cur>max2):
        max2=cur


print("Second largest: %s " % max2)
print("Largest: %s" % max1)