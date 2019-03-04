def fun(a,b):
    try:
        return a/b
    except:
        return None
def Even_check(a=0):
    try:
        if a%2 ==0:
            return 'Even'
        else:
            return 'Odd'
    except:
        return None
