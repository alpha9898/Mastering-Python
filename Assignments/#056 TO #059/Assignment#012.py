def calc (n1 ,n2 , procces = "a") :
  if procces.lower() == "add" or procces[0].lower()=="a":
    return n1 + n2
  
  elif procces.lower() == "subtract" or procces[0].lower()=="s":
    return n1 - n2

  elif procces.lower() == "devide" or procces[0].lower()=="d":
    return n1 / n2

  else :
    print("ERORR")

print(calc(1,2))

print("=" * 30)


def add(*numbers):
    total = 0
    for num in numbers:
        if num == 10:
            continue
        elif num == 5:
            total -= num
        else:
            total += num
    return total


print(add(10, 20, 30, 10, 15)) # 65
print(add(10, 20, 30, 10, 15, 5, 100)) # 160

print("=" * 30)


def show_skills( name ,*skills):
      if len(skills) > 0 :
        print(f"Hello {name} Your Skills Is : ")
        for skill in skills :
          print(f"- {skill}")
      else : 
        print(f"\" Hello {name} You Have No Skills To Show \"")

show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")

print("=" * 30)


def say_hello (name = "Unknown" , age = "Unknown", country = "Unknown") :
    return f"Hello {name} Your Age Is {age} And You Live In {country}"

print(say_hello("Osama", 38, "Egypt"))
print(say_hello())

print("=" * 30)
