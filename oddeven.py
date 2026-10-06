import sys
def evenorodd(num):
    if(num% 2==0):
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    num = int(sys.argv[1])
    print("even or odd", evenorodd(num))