pairs = [[1, 2, 3], [1, 1, 1], [1, 3, 4], [2, 2, 2]]

same_count = 0

for x, y, z in pairs:
    if x == y == z:
        same_count += 1

same_count
a = list(range(-2, 2))
b = list(range(3))
# for _ in range(3):
#     print("Go bear!")

test = [1, 34, 52, 45, 2]

total = 0
for i in test:
    total += i


def mysum(L):
    if L == []:
        return 0
    else:
        return L[0] + mysum(L[1:])


# a = input()
# print(a)

odds = [1, 5, 3, 4, 6, 10]

city = "cheng du"


def reverse(L):
    if len(L) == 1:
        return L
    else:
        return reverse(L[1:]) + L[0]
