def gcd(x, y):
    if x == 0 or y == 0: 
         return max(x, y)
    else:
     if x > y:
        return gcd(x - y, y)
     else:
        return gcd(x, y - x)
     

print("gcd(56, 98) = " + str(gcd(56, 98)))