import random as rd 

gen_num = rd.randint(1, 9)
print("generated number: ", gen_num)
count = 0
a = 0
while a != 1:
    count += 1
    guess = int(input("guess a number between 1 - 9: "))

    if gen_num < guess:
        print("guessed number too high...")
    elif gen_num > guess:
        print("guessed number too low...")
    elif gen_num == guess:
        print("guessed exactly right number.....")
        break
    else:
        print("invalid input...")

    con_e = int(input("do you want to continue? \n1.yes\n2.no\n"))
    if con_e == 1:
        print("let continue...try again")
    elif con_e == 2:
        print("exit...")
        a = 1
if a == 1:
    print(f"you quiteted after {count} Guesses, and you were this far: {abs(gen_num-guess)}")
print(f"game finished after {count} guesses...")
