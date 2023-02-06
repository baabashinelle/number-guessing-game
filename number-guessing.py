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
guesses = 0


while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit(): #checking if input is a digit
        user_guess = int(user_guess)
    else:
        print("Kindly type a number next time")
        continue #goes back to the top of the loop

    if user_guess == r_number:
        print("You got it!")
        break #stops the loop
    else:
        if user_guess > r_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

print("You got it right in", guesses, "guesses")
