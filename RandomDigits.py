import random

pin_code = random.randint(1000, 9999)
user = int(input("Enter your code from 4 digits: \n"))
if len(str(user)) != 4:
    print("You can use only 4 digits")


elif user == pin_code:
    print(pin_code, "good matching")

elif user != pin_code:
    print(pin_code, "Try again")

else:
    print(user, "Not accepted")
