a = [1, 2, 3, 4, 5, 6]
b = [
    [1, 2],
    [2, 3],
    [4, 5]
]


# print(a[:-1])
# print(a[len(a)-1])

# print(b[:2])

def cluster_age(age):
    if age <= 30:
        return 1
    elif 30 < age <= 40:
        return 2
    elif 40 < age <= 50:
        return 3
    elif age > 50:
        return 4


def cluster_balance(balance):
    if balance < 0:
        return 1
    elif 0 <= balance < 1000:
        return 2
    elif balance >= 1000:
        return 3

# print(cluster_age(41))
# print(cluster_balance(-50))


for i in range(0,10):
    print(i)
