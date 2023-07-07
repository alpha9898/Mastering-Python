my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
print(unique_list)
print(type(my_list))
unique_list.remove(5)
print(unique_list)
print("=" * 30)

nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums | letters)
print(nums.union(letters))
nums.update(letters)
print(nums)
print("=" * 30)

my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
print("=" * 30)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print('=' * 30)

skills = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%",
    "AI": "20%"
}

skills.update({"C": "0%"})
key = list(skills.keys())


print(f"{key[0]} Progress Is {skills[key[0]]}")
print(f"{key[1]} Progress Is {skills[key[1]]}")
print(f"{key[2]} Progress Is {skills[key[2]]}")
print(f"{key[3]} Progress Is {skills[key[3]]}")
print(f"{key[4]} Progress Is {skills[key[4]]}")

