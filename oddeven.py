import sys
def evenorodd(num):
    if(num% 2==0):
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    num = int(sys.argv[1])
    num1 = int(sys.argv[2])
    num2 = int(sys.argv[3])
    print("even or odd", evenorodd(num))
    print("even or odd", evenorodd(num1))
    print("even or odd", evenorodd(num2))