
import random
def randomList(n:int):
    llist = []
    for i in range(n):
        llist.append(random.randint(1,100))
    return llist
if __name__ == '__main__':
    print(randomList(20))


