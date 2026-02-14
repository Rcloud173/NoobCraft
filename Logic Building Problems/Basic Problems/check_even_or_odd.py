def isEven(n):
    # taking bitwise and of n with 1 
    if (n & 1) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = 15
    if isEven(n):
        print("true")
    else:
        print("false")