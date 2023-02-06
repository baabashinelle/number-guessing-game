import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): #checking if input is a digit
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number")
    quit()

r_number = random.randrange(top_of_range)
print(r_number)
