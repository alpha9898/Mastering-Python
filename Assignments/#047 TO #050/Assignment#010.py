# num = int(input("Enter a number: ").strip())
# count = 0

# if num > 0:
#   while num > 0:
#     num -= 1
#     if num == 0:
#       break
#     if num == 6:
#       continue
#     print(num)
#     count += 1
#   print("=" * 30)
#   print(f"{count} numbers printed")

# else:
#   print("plesse enter a number greater than 0")
# print("=" * 30)



# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif", "amar", "Ahmed", "Eman", "Sherif", "Ama"]
# discarded = 0
# index = 0

# while index < len(friends):
#   if friends[index] != friends[index].lower() :
#       print(friends[index])
#       index+=1
    
#   else:
#     discarded += 1
#     index += 1
#     continue
# else:
#   print("=" * 30)
#   print(f"{discarded} names discarded")
# print("=" * 30)



# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills:
#   print(skills.pop(0))
# print("=" * 30)


# print("#" * 50)
# print(" Hello , You Can Now ADD your Friends ".center(50 , "#"))
# print("#" * 50)

my_friends = []
max_friends = 4

while max_friends > 0 :
  name = input("plese enter a name").strip()

  if name == name.upper() :
    print("ERORR")

  elif name == name.lower() :
    name.capitalize()
    print(f"Friend {name} Added => 1st Letter Become Capital")
    my_friends.append(name)
    max_friends -= 1

  elif name == name.capitalize():
    print(f"Friend {name} Added")
    my_friends.append(name)
    max_friends -= 1

  else : 
    print("Enter A valid Name Please : ")
    print(f"Names Left in List Is {max_friends}")

else : 
    print("List Is Full Now")
    print(my_friends)