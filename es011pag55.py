x = [0, 1, 2, 3, 5, 6, 7, 8]

lung = len(x) // 2

x1 = x[:lung]
print(x1)

x2 = x[lung:]
print(x2)

x1.append(5)
print(x1)
