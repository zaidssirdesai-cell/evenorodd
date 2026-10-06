def evenorodd(num):
    if(num% 2==0):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

if __name__ == "__main__":
    num = 27
    print("even or odd", evenorodd(num))