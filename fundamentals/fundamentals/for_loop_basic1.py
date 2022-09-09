"""
Basic - Print all integers from 0 to 150.

Multiples of Five - Print all the multiples of 5 from 5 to 1,000

Counting, the Dojo Way - Print integers 1 to 100.
If divisible by 5, print "Coding" instead.
If divisible by 10, print "Coding Dojo".

Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

Flexible Counter - Set three variables: lowNum, highNum, mult.
Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""

for x in range(0,151):
    print(x)

for y in range(5,1005,5):
    print(y)

for a in range(1,101):
    print(a)
    if a%5==0:
        print('coding')
    if a%10==0:
        print('dojo')

sum=0
for w in range (1,500001,2):
    sum+=i
print(sum)        

for b in range(2018,0,-4):
    print(b)

lowNum = 2
highNum = 100
mult = 4
for f in range(lowNum, highNum):
    if f%mult==0:
        print(f)
