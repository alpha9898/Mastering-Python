print("Choose One Of them => + Or - Or * Or / Or %")
num1 = input("Enter First Number: ").strip()
num2 = input("Enter Second Number: ").strip()
operation = input("Enter Operation: ").strip()

if operation == "+":
    print(f"{num1} + {num2} = {int(num1) + int(num2)}")
elif operation == "-":
    print(f"{num1} - {num2} = {int(num1) - int(num2)}")
elif operation == "*":
    print(f"{num1} * {num2} = {int(num1) * int(num2)}")
elif operation == "/":
    print(f"{num1} / {num2} = {int(num1) / int(num2)}")
elif operation == "%":
    print(f"{num1} % {num2} = {int(num1) % int(num2)}")
else:
    print("Erorr")
print("=" * 30)

age = int(input("What\'s Your Age ?"))
print("App Is Suitable For You" if age >= 16 else "App Is Not Suitable For You")
print("=" * 30)

age = int(input("What\'s Your Age ?"))

months = age * 12
weeks = months * 4
days = weeks * 7
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

if age >10 and age < 100:
    print("your age is good")
    print(f"Your Age In Months Is {months} Months")
    print(f"Your Age In Weeks Is {weeks} Weeks")

else:
    print("your age is not good")
print("=" * 30)

country = input("Input Your Country ").strip()
countries = ["Egypt", "Palestine", "Syria","Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
    print(
        f"Your Country Eligible For Discount And The Price After Discount Is {price - discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is {price}")