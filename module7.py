import math

def areaOfCircle(r):
    area= 22/7 * r
    return area


def CheckRange(n):
    lists= []
    for i in range(1,10):
        lists.append(i)
    if n not in lists:
        print("Not in range")
    else:
        print("In range")

def multiply(l):
    m= l[0] * l[1]
    for i in range(2,len(l)):
        m= m* l[i]
        
    return m

def unique(c):
    newlists= []
    for i in c:
        if i not in newlists:
            newlists.append(i)
            
    return newlists
        
radius= int(input("Enter Radius"))
print(areaOfCircle(radius))

number= int(input("Enter a number to check range"))
print(CheckRange(number))
                  
lists= [5,2, 7, -1]
lists2=[1, 3, 3, 3, 6, 2, 3, 5]
print(multiply(lists))
print(unique(lists2))
