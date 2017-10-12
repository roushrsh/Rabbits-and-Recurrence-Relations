n = 35
k = 5
count = 2
initial = 1
initial2 = 1

def wabbits(twoB4, B4, now):
    global count, k, n
    count = count+1
    if (count == n):
        print (now)
        return
    wabbits(B4, now, (now + B4*k))


if (n==1):
    print initial
elif (n==2):
    print initial
elif (n>2):
    wabbits(initial, initial2, (initial2+k))






#
#1
#1
#4
#7
#19
