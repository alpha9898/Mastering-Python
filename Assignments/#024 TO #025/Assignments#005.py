name = "amar",
print(name)
print(type(name))
print("=" * 30)

friends = ("Osama", "Ahmed", "Sayed")
friends_list = list(friends)
friends_list[0] = "Elzero"
friends = tuple(friends_list)
print(friends)
print(type(friends))
print(len(friends))
print("=" * 30)

nums = (1, 2, 3)
letters = ("A", "B", "C")
m = nums + letters
print(f"nums_and_letters_one = {m}")
print(len(m))
print("=" * 30)

my_tuple = (1, 2, 3, 4)

a , b , _, d = my_tuple
print(a)
print(b)
print(d)
print("=" * 30)