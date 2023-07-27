sp = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5]
sl = dict()

for i in sp:
    a = i ** i
    sl[i] = a
    
print(sl)
