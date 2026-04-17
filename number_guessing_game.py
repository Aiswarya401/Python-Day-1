import  random

from matplotlib.pylab import number
print("Welcome to Number Guessing Game!")

randno=random.randint(1,10)
attempts=0

while True:
    guess=int(input("Enter your guess :"))
    attempts+=1

    if guess==randno:
        print("YOU WON!")
        print("Number of attempts:", attempts)
        break
        
    
    elif abs(guess - randno) <= 5:
        print("You are CLOSE, try another guess")
    else:
        print("You are FAR, try another guess")