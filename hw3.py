"""Joseph Gargiulo"""
"""I pledge my honor that I have abided by the Stevens Honor System"""
#Problem 1
def addOne(l):
    if l == []:
        return []
    else:
        return [l[0]+1] + addOne(l[1:])
#Problem 2
def explode(s):
    """return a list of characters with a string of length 1"""
    if s == '':
        return[]
    else:
        return [s[0]] + explode(s[1:])
#Problem 3
def even(x):
    if x % 2 == 0:
        return True
    else:
        return False 
def odd(x):
    if x % 2 != 0:
        return True
    else:
        return False

def myFilter(func,l):
    """returns a list of all the values that would return true if ran in the function f"""
    if l == []:
        return []
    elif func(l[0]) == False:
       return myFilter(func, l[1:])
    else:
        return [l[0]] + myFilter(func, l[1:])
        
#Problem 4
def sumPos(L):
    if L == []:
        return 0
    elif L[0] < 0:
        return 0 + sumPos(L[1:])
    else:
        return L[0] + sumPos(L[1:])
