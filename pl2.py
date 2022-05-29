# Substring of last element
def substring(l1):
    return l1[len(l1)-2] in l1[len(l1)-1] and l1[len(l1)-2] != l1[len(l1)-1]


if __name__ == "__main__":
    l1 = []
    try:
        while True:
            l1.append(input())
    except:
        print(substring(l1))
