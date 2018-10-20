import asyncio
import math


async def is_prime(x, result):
    if x == 1:
        return
    for i in range(2, x):
        if i % 100 == 0:
            await asyncio.sleep(1)
        if x % i == 0:
            return
    result[0] += x
    return


if __name__ == "__main__":
    n = 10
    m = 1000000
    loop = asyncio.get_event_loop()
    result = [0]
    loop.run_until_complete(asyncio.gather(
        *[is_prime(i, result) for i in range(n, m)]
    )
    )
    loop.close()
    print(result[0])
