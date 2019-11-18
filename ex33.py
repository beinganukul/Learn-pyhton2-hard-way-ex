i=0
numbers=[]

while i<6:
    print "At the top i is %d" %i
    numbers.append(i)

    i+=1
    print "Numbers now:", numbers
    print "At the buttom i is %d"%i

print "The numbers:\n"

for num in numbers:
    print num