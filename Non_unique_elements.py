#Author Akkash
#Non-unique elements

def non(a):                   #create a function
   c = []                     #creating a new list
   for x in a:                
       if a.count(x) > 1:     #a method used to count the no. of times the element repeated
           c.append(x)        #method used to add an element into the list
           return c
 
non([1,2,3,1,3])              #calling the function
