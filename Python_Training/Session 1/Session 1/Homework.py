#!/usr/bin/env python
# coding: utf-8

# In[1]:


def changeme( mylist ):
   # "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return mylist

# Now you can call changeme function
mylist = [10,20,30];
newlist=changeme( mylist );
print ("Values outside the function: ", mylist)


# In[2]:


def changeme( mylist ):
   # "This changes a passed list into this function"

    mylist=[1,2,3,4]
   
    print ("Values inside the function: ", mylist)
    return mylist

# Now you can call changeme function
mylist = [10,20,30];
newlist=changeme( mylist );
print ("Values outside the function: ", mylist)


# In[4]:


# define a class
class Shape(object):
    
    # "__new__" method is omitted
    
    # initializer, "self" refers to the object itself
    def __init__(self, color):  
        # class variable is assigned with input value
        self.color = color               
        print('color is set to: ', self.color)
        
    # function (or method) of the class
    # note the first argument referencing the class object 
    # must be there
    def changeColor(x, newColor):   
        x.color=newColor
        return "New color is "+x.color
    
    # note "self" must be in every function of the class 
    
# use the class
# initiate a shape instance. 
# "self" in the class refers to "myshape"
myshape=Shape('red') 

# call class attribute
print(myshape.color)  

# invoke class method "changeColor"
print(myshape.changeColor('blue'))  

# check what color the instance has
print(myshape.color)  


# In[5]:


class Circle(Shape):
    
    def __init__(self, color, diameter):
        
        # call superclass' constructor
        Shape.__init__(self, color)
        
        # initialize another variable
        self.diameter = diameter
    
    # define a new function getArea 
    def getArea(self):
        return (3.1416*self.diameter/2**2)
    
# use Square class
my_circle = Circle('green', 4)

# get square area
print(my_circle.getArea())

# get square color
print(my_circle.color)


# In[ ]:




