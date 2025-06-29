import random
secret_number = random.randint(1, 10)

guess =int(input("Guess a number between 1 and 10: "))

match guess:
        case x if x == secret_number:
            print("Congratulations, you guessed it!")
        case x if x > secret_number:
            print("Good job")
        case x if x < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
    
play_again = input("Do you want to play again? yes/no: ").strip().lower()
if play_again != "Yes":
    print("Guess a number! please!")
else:
     print
    
        




