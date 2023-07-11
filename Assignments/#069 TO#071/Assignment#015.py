values = (0, 1, 2)

if any(values):

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var]

if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good")

else:

  print("Bad")

# !Good

v = 40  
#?? v = 40

my_range = list(range(v))

print(sum(my_range, v) + pow(v, v, v)) 



n = 20

l = list(range(n))

if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")


def my_max (numbers) :
    max = 0 
    for number in numbers :
        if max < number :
            max = number 
    return max

def my_min (numbers) :
    min = 0 
    for number in numbers :
        if min > number :
            min = number 
    return min

def my_all (l) :
    cond = True
    for e in l :
        if bool(e) == True :
            cond = True 
        else :
            cond = False
            break
    return cond

def my_any (l) :
    cond = True
    for e in l :
        if bool(e) == True :
            cond = True 
            break
        else :
            cond = False
    return cond

# # my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False

# # my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# # my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max([10, 100, -20, -100, 50, 700])) # 700