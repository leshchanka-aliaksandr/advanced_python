def pack(iterable, limit):
    current_weight = 0
    bag = []
    for i in iterable:
        if current_weight + i[2] <= limit:
            bag.append(i[0])
            current_weight += i[2]
        else:
            continue
    return bag


if __name__ == "__main__":
    items = [
        ["map", 9, 150],
        ["compass", 13, 35],
        ["water", 153, 200],
        ["sandwich", 50, 160],
        ["glucose", 15, 60],
        ["tin", 68, 45],
        ["banana", 27, 60],
        ["apple", 39, 40],
        ["cheese", 23, 30],
        ["beer", 52, 10],
        ["suntan cream", 11, 70],
        ["camera", 32, 30],
        ["T-shirt", 24, 15],
        ["trousers", 48, 10],
        ["umbrella", 73, 40],
        ["waterproof trousers", 42, 70],
        ["waterproof overclothes", 43, 75],
        ["note-case", 22, 80],
        ["sunglasses", 7, 20],
        ["towel", 18, 12],
        ["socks", 4, 50],
        ["book", 30, 10]
    ]

    bag = pack(sorted(items, key=lambda x: x[2] / x[1], reverse=True), 400)
    print(bag)
