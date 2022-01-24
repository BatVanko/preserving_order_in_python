

x = input().split(" ")

print(*sorted(set(x), key=x.index))
