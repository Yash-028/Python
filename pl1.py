# Integer check :
def check(num):
    if num > 256 and num % 34 == 4:
        return True
    else:
        return False


if __name__ == "__main__":
    num = int(input("Enter number for check : "))
    print(check(num))
