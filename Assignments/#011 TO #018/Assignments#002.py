name = "Amar"
age = 20
country = "Egypt"

print("Hello \'%s\', How You Doing \\ \"\"\" Your Age Is \" %d \"\" + And Your Country Is: %s" %(name, age, country))
print("=" * 30)


print("Hello \'%s\', How You Doing \\\n\"\"\" Your Age Is \" %d \"\" +\nAnd Your Country Is: %s" %(name, age, country))
print("=" * 30)


namee = 'Elzero'
print("Second Letter Is : " + namee[1])
print("Third Letter Is : " + namee[2])
print("Last Letter Is : " + namee[-1])


print(namee[1:4])
print(namee[::2])
print(name[-2::-2])


naame = "#@#@Elzero#@#@"
print(naame.strip("#@"))


num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))


name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@"))
print(name_two.rjust((8 + len(name_two)), "@"))


name_onee = "OSamA"
name_twoo = "osaMA"

print(name_onee.swapcase())
print(name_twoo.swapcase())


msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))


nameee = "Elzero"
print(nameee.index("z"))


msgg = "I <3 Python And Although <3 Elzero Web School"
print(msgg.replace("<3", "Love", 1))


msggg = "I <3 Python And Although <3 Elzero Web School"
print(msggg.replace("<3", "Love"))


naamee = "Amar"
aggee = 20
countryy = "Egypt"

print(f"My Name Is  {naamee}, And My Age Is {aggee}, And My Country Is {countryy}")