num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Choose: ")

if choice == "1":
    print(num1 + num2)

elif choice == "2":
    print(num1 - num2)

elif choice == "3":
    print(num1 * num2)

elif choice == "4":
    print(num1 / num2)