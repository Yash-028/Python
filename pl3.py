from operator import truediv


def sum(l1):
    sum = 0
    for i in l1:
        sum = int(sum + i)
    if sum == len(l1):
        return True
    else:
        return False


if __name__ == "__main__":
    l1 = []
    try:
        while True:
            l1.append(int(input()))
    except:
        print(sum(l1))
