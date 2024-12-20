#Random guessing game
import random
rand = random.randint(0,10)
ans = int(input("Input a num: "))
if ans == rand:
    print("Correct!")
else:
    print("Better luck next time!") 
end()