import os
x = 1 
while (x <= 50) :
    if x == 25 :
        file = open(f"special-text" , "x")
    else :
        file = open(f"txt{x}" , "w")
        file.write(f"Elzero Web School => {x}\n")
    x+=1

print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
filepy = open("assign.py" , "r")
print(filepy.name)


file = open("txt1" , "a")
file.write("Appended => Elzero Web School\n" * 50)


file = open("txt1" , "r")
l = file.readlines()
print(len(l))

string = "".join(l)
count_l = 0 
print(len(string)) 

for l in string :
    if l == "l" or l == "L" :
        count_l += 1
else :
    print(count_l)



r = 50 
while r > 40 :
    os.remove(rf"c:\Users\ezemo\OneDrive\Desktop\Python\txt{r}")
    r -= 1
else :
    print("reomving Done")