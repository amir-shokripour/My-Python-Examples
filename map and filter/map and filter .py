# map
# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
# Syntax -->  map(function, iterables)
# convert the map into a list, for readability
# also you can use for loop
def power_two(number):
    return number ** 2


num_list = [1, 2, 3, 4, 5]

x = map(power_two, num_list)
print(list(x)) # [1, 4, 9, 16, 25]

# lambda
x = list(map(lambda num: num ** 2, num_list))
print(x) # [1, 4, 9, 16, 25]

#for loop
x = map(power_two, num_list)
for i in x:
    print(i)
# -->
# 1
# 4
# 9
# 16
# 25

# -------------------------------------
# filter
# The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
# Syntax --> filter(function, iterable)
# convert the filter into a list, for readability
# also you can use for loop

score = [10, 20, 15, 19, 17, 14]
def myfunc(a):
    if a >= 15:
        return True
    return False 

x = list(filter(myfunc , score))
print(x) #[20, 15, 19, 17]

#lambda
x = list(filter(lambda a : a >= 15 , score))
print(x) #[20, 15, 19, 17] 

#for loop
x = filter(lambda a : a >= 15 , score)
for i in x:
    print(i)
# -->
# 20
# 15
# 19
# 17
