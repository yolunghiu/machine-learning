# while
i = 0
while i < 5:
    print('hello world')
    i += 1

# for
for i in range(10):
    print('----')
    if i == 3:
        break
    print(i)

# continue
for i in range(10):
    print('----')
    if i == 3:
        continue
    print(i)
