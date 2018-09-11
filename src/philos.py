from multiprocessing import Lock
from multiprocessing import Process
import time


def philo(id: int, table: list, left: int, right: int):
    table[left].acquire()
    print(f"{id} take first fork")
    time.sleep(1)
    table[right].acquire()
    print(f"{id} take second fork")
    time.sleep(1)
    print(f"{id} start eating")
    time.sleep(2)
    table[right].release()
    table[left].release()
    print(f"{id} stop eating")


if __name__ == "__main__":
    n = 5
    table = []
    philos = []
    for i in range(n):
        table.append(Lock())
    philos.append(
        Process(target=philo, args=(0, table, 1, 0))
    )
    for i in range(1, n):
        philos.append(
            Process(target=philo, args=(i, table, i, (i + 1) % n))
        )

    for p in philos:
        p.start()

    for p in philos:
        p.join()

    print("Finish")
