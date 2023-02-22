class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for n in nums: 
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums: 
            self.result -=n 
        return self

# create an instance:

md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5

#   md.add(2)
#       return instance of MathDojo which is md 
#       md instance now has a result attribute=2 
#       md.result = 2
#   md.add(2,5,1)
#       return instance of MathDojo 
#       md.result = 10 
#       return md 
#   md.subtract(3,2)
#       md.result=5 
#       return md 
#   x is equal to the instance md invoking these methods,   and then at the end it accesses the result attribute (.result) of md 
#   So last line is x = md.result
#   and we know md.result=5 after calling these methods

