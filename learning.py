# (== to check that the values are the same#
# (!= to check that two values are not equel #
# < to check that a value is less than #
# > to check that a value is greater than #
# <= to check that a value is less than or equal to #
# >= to check that a value is greater than or equal to


"""
LOGICAL OPERATIONS

and = both conditions must be true
or = one of the conditions can be true
not = the reverse of the condition

"""
age = 10
x = 10
y = 20

access = ( age > 9) and (age < 20)
print(access)

demo = (y > x) or (y == age)
print(demo)

# the arguement here is that y is not greater tha x
result = not (y > x)