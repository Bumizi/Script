output = 'NO'
count = 0
for k in range(6):
    s = input()
    l = s.split()
    l = [eval(i) for i in l]
    l.sort()
    for m in range(2):
        for n in range(3):
            if l[m+n] + 1 == l[m+n+1]:
                print(count)
                count += 1
        if count == 3:
            count = 0
            output = 'YES'
            break
        count = 0
        output = 'NO'
    print(output)