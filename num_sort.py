
a = [1,3,4,3,2,3,5,6,7,9,6,5,3]
a.sort()
a.reverse()
sum = 0
for i in a:
    sum = sum + i
print a, sum/len(a)
