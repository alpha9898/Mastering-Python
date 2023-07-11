from functools import reduce

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

def remove_chars(name):
  return name[1:-1]

cleaned_list = map(remove_chars, friends_map)
for name in cleaned_list:
    print(name)


print("=" * 30)


friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def get_names (name) :
  return name[-1] == "m" 

names = filter(get_names,friends_filter)
for name in names:
  print(name)

print("=" * 30)


nums = [2, 4, 6, 2]

def multi (num1 , num2) :
  return num1 * num2

multiplcation  = reduce(multi , nums)
print(multiplcation)

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
enum_skills = enumerate(reversed(skills) , 50) 
for counter , skill in  enum_skills:
  if type(skill) != str :
    continue
  else :
    print(f"{counter} - {skill}")