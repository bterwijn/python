import random
import time

def main():
    random.seed(0)  # same random number each run
    n = 1000000
    container = make_container(n)
    search_items(n, container)

def make_container(n):
    return set(random_item(n) for i in range(n))  # set
    #         [random_item(n) for i in range(n)]  # list

def random_item(n):
    return random.randrange(0, n)

def search_items(n, container, tries=1000):
    start_time = time.time()
    count = 0
    for i in range(tries):
        item = random_item(n)
        if item in container:
            count += 1
    stop_time = time.time()
    print("average search time:", (stop_time - start_time) / tries, "secs")
    print(f"found: {100*count/tries}%")

main()
