def collatz(num):
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int(3 * num + 1)
    else:
        print(1)

def main():
    num = int(input('Input an integer: '))
    collatz(num)
main()
