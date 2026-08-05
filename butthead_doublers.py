num = 105263157894736842
# print(num * 2)

num = 100000000000000000
while str(num * 2) != str(num)[-1] + str(num)[0:-1]:
    num += 1

print(num)
